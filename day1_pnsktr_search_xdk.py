#!/usr/bin/env python3
"""
X API PPU Pilot - Day 1 (Official XDK Version)
Testing the new official Python XDK for PNSKTR search
"""

import os
import csv
from datetime import datetime
from dotenv import load_dotenv
from xdk import Client

# Load environment variables
load_dotenv()

# Configuration
BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')
SEARCH_QUERIES = ['PNKSTR', 'PNKSTR OR pnkstr OR Pnkstr']  # Variations to catch more
MAX_RESULTS = 100  # Per query
OUTPUT_FILE = f'data/pnsktr_tweets_xdk_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
LOG_FILE = f'logs/xdk_api_calls_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'

# API call counter
api_calls = 0

def log_api_call(endpoint, params):
    """Log each API call for cost tracking"""
    global api_calls
    api_calls += 1
    with open(LOG_FILE, 'a') as f:
        f.write(f"[{datetime.now().isoformat()}] Call #{api_calls}: {endpoint}\n")
        f.write(f"  Params: {params}\n\n")

def search_tweets_xdk(client, query, max_results=100):
    """Search for tweets using official XDK"""
    print(f"\n🔍 Searching for: '{query}'")

    try:
        log_api_call('posts.search_recent', {
            'query': query,
            'max_results': max_results
        })

        # Using the official XDK - simpler API!
        response = client.posts.search_recent(
            query=query,
            max_results=max_results,
            tweetfields=['created_at', 'public_metrics', 'author_id', 'lang'],
            expansions=['author_id'],
            userfields=['username', 'name', 'verified']
        )

        if not response or not hasattr(response, 'data') or not response.data:
            print(f"  ⚠️  No tweets found for '{query}'")
            return []

        # Build user lookup dict from includes
        users = {}
        if hasattr(response, 'includes') and response.includes and 'users' in response.includes:
            users = {user['id']: user for user in response.includes['users']}

        tweet_data_list = []
        for tweet in response.data:
            # Tweets come as dicts in XDK
            user = users.get(tweet.get('author_id'))

            tweet_data = {
                'query': query,
                'tweet_id': tweet.get('id'),
                'created_at': tweet.get('created_at', ''),
                'text': tweet.get('text', '').replace('\n', ' ').replace('\r', ' '),
                'author_id': tweet.get('author_id', ''),
                'author_username': user.get('username') if user else 'unknown',
                'author_name': user.get('name') if user else 'unknown',
                'author_verified': user.get('verified', False) if user else False,
                'likes': tweet.get('public_metrics', {}).get('like_count', 0),
                'retweets': tweet.get('public_metrics', {}).get('retweet_count', 0),
                'replies': tweet.get('public_metrics', {}).get('reply_count', 0),
                'quotes': tweet.get('public_metrics', {}).get('quote_count', 0),
                'impressions': tweet.get('public_metrics', {}).get('impression_count', 0),
                'language': tweet.get('lang', '')
            }
            tweet_data_list.append(tweet_data)

        print(f"  ✅ Found {len(tweet_data_list)} tweets")
        return tweet_data_list

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
    print("X API PPU PILOT - DAY 1: PNSKTR SEARCH (Official XDK)")
    print("="*70)

    # Authenticate using official XDK
    if not BEARER_TOKEN:
        print("\n❌ Error: TWITTER_BEARER_TOKEN not found in .env file")
        print("   Please copy .env.example to .env and add your token")
        return

    client = Client(bearer_token=BEARER_TOKEN)

    print("\n✅ Authenticated with X API v2 (Official Python XDK)")
    print("   XDK Version: 0.2.2b0")

    # Search for each query
    all_tweets = []
    for query in SEARCH_QUERIES[:1]:  # Start with just first query
        tweets = search_tweets_xdk(client, query, max_results=MAX_RESULTS)
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
    print("\n🎯 XDK Benefits:")
    print("   ✓ Simpler authentication")
    print("   ✓ Automatic pagination handling")
    print("   ✓ Built-in rate limit management")
    print("   ✓ Type-safe responses with Pydantic")
    print("\n" + "="*70)

if __name__ == '__main__':
    main()
