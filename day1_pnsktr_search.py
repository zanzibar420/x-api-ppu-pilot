#!/usr/bin/env python3
"""
X API PPU Pilot - Day 1
Simple search test for PNSKTR mentions
"""

import os
import csv
import tweepy
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')
SEARCH_QUERIES = ['PNKSTR', '$PNKSTR']
MAX_RESULTS = 100  # Per query (10-100 allowed)
OUTPUT_FILE = f'data/pnsktr_tweets_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
LOG_FILE = f'logs/api_calls_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'

# API call counter
api_calls = 0

def log_api_call(endpoint, params):
    """Log each API call for cost tracking"""
    global api_calls
    api_calls += 1
    with open(LOG_FILE, 'a') as f:
        f.write(f"[{datetime.now().isoformat()}] Call #{api_calls}: {endpoint}\n")
        f.write(f"  Params: {params}\n\n")

def search_tweets(client, query, max_results=100):
    """Search for tweets with engagement metrics"""
    print(f"\n🔍 Searching for: '{query}'")

    # Tweet fields to retrieve
    tweet_fields = ['created_at', 'public_metrics', 'author_id', 'lang']
    expansions = ['author_id']
    user_fields = ['username', 'name', 'verified']

    try:
        # Search recent tweets
        log_api_call('search_recent_tweets', {
            'query': query,
            'max_results': max_results,
            'tweet_fields': tweet_fields
        })

        response = client.search_recent_tweets(
            query=query,
            max_results=max_results,
            tweet_fields=tweet_fields,
            expansions=expansions,
            user_fields=user_fields
        )

        if not response.data:
            print(f"  ⚠️  No tweets found for '{query}'")
            return []

        tweets = []
        users = {user.id: user for user in response.includes.get('users', [])}

        for tweet in response.data:
            user = users.get(tweet.author_id)

            tweet_data = {
                'query': query,
                'tweet_id': tweet.id,
                'created_at': tweet.created_at,
                'text': tweet.text.replace('\n', ' ').replace('\r', ' '),
                'author_id': tweet.author_id,
                'author_username': user.username if user else 'unknown',
                'author_name': user.name if user else 'unknown',
                'author_verified': user.verified if user else False,
                'likes': tweet.public_metrics['like_count'],
                'retweets': tweet.public_metrics['retweet_count'],
                'replies': tweet.public_metrics['reply_count'],
                'quotes': tweet.public_metrics['quote_count'],
                'impressions': tweet.public_metrics.get('impression_count', 0),
                'language': tweet.lang
            }
            tweets.append(tweet_data)

        print(f"  ✅ Found {len(tweets)} tweets")
        return tweets

    except Exception as e:
        print(f"  ❌ Error: {e}")
        return []

def print_engagement_summary(all_tweets):
    """Print engagement metrics summary"""
    if not all_tweets:
        print("\n⚠️  No tweets to analyze")
        return

    total_tweets = len(all_tweets)
    total_likes = sum(t['likes'] for t in all_tweets)
    total_retweets = sum(t['retweets'] for t in all_tweets)
    total_replies = sum(t['replies'] for t in all_tweets)
    total_quotes = sum(t['quotes'] for t in all_tweets)

    avg_likes = total_likes / total_tweets
    avg_retweets = total_retweets / total_tweets
    avg_replies = total_replies / total_tweets

    print("\n" + "="*70)
    print("ENGAGEMENT METRICS SUMMARY")
    print("="*70)
    print(f"\nTotal Tweets: {total_tweets}")
    print(f"\nTotal Engagement:")
    print(f"  Likes:     {total_likes:,}")
    print(f"  Retweets:  {total_retweets:,}")
    print(f"  Replies:   {total_replies:,}")
    print(f"  Quotes:    {total_quotes:,}")
    print(f"\nAverage per Tweet:")
    print(f"  Likes:     {avg_likes:.1f}")
    print(f"  Retweets:  {avg_retweets:.1f}")
    print(f"  Replies:   {avg_replies:.1f}")

    # Top 5 by engagement
    sorted_tweets = sorted(all_tweets, key=lambda x: x['likes'] + x['retweets'], reverse=True)
    print(f"\nTop 5 Most Engaged Tweets:")
    for i, tweet in enumerate(sorted_tweets[:5], 1):
        total_engagement = tweet['likes'] + tweet['retweets'] + tweet['replies']
        print(f"\n{i}. @{tweet['author_username']} ({total_engagement:,} total engagement)")
        print(f"   {tweet['text'][:100]}...")
        print(f"   ❤️ {tweet['likes']}  🔁 {tweet['retweets']}  💬 {tweet['replies']}")

def save_to_csv(tweets, filename):
    """Save tweets to CSV file"""
    if not tweets:
        print("\n⚠️  No tweets to save")
        return

    fieldnames = [
        'query', 'tweet_id', 'created_at', 'text',
        'author_id', 'author_username', 'author_name', 'author_verified',
        'likes', 'retweets', 'replies', 'quotes', 'impressions', 'language'
    ]

    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(tweets)

    print(f"\n💾 Saved {len(tweets)} tweets to: {filename}")

def main():
    print("="*70)
    print("X API PPU PILOT - DAY 1: PNSKTR SEARCH")
    print("="*70)

    # Authenticate
    if not BEARER_TOKEN:
        print("\n❌ Error: TWITTER_BEARER_TOKEN not found in .env file")
        print("   Please copy .env.example to .env and add your token")
        return

    client = tweepy.Client(bearer_token=BEARER_TOKEN)
    print("\n✅ Authenticated with X API v2")

    # Search for each query
    all_tweets = []
    for query in SEARCH_QUERIES:
        tweets = search_tweets(client, query, max_results=MAX_RESULTS)
        all_tweets.extend(tweets)

    # Print summary
    print_engagement_summary(all_tweets)

    # Save results
    save_to_csv(all_tweets, OUTPUT_FILE)

    # Final stats
    print("\n" + "="*70)
    print("API USAGE SUMMARY")
    print("="*70)
    print(f"\nTotal API Calls: {api_calls}")
    print(f"Log file: {LOG_FILE}")
    print(f"\n💰 Cost Tracking: Check console.x.com for PPU charges")
    print("\n" + "="*70)

if __name__ == '__main__':
    main()
