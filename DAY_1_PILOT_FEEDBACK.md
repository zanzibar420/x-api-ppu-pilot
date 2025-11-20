# X API PPU Pilot - Day 1 Feedback

**Date**: November 20, 2025
**Tester**: @ZanzibarVenturz
**Project**: Token Community Intelligence Platform

---

## What We Built

✅ **PNSKTR Twitter Search Tool**
- Authenticated with X API v2 using Bearer Token
- Searched for "PNKSTR" mentions
- Retrieved 100 recent tweets with full engagement metrics
- Logged all API calls for cost tracking
- Saved results to CSV for analysis

**Tech Stack**: Python 3.13, Tweepy 4.16.0, X API v2

---

## Results

### Tweets Retrieved
- **Query**: "PNKSTR"
- **Results**: 100 tweets
- **Time period**: Last 7 days (recent search)

### Engagement Summary
- Total likes: 405
- Total retweets: 483
- Total replies: 43
- Average engagement: 4.8 retweets, 4.0 likes per tweet

### Top Finding
**@ApeNuke** with 77 total engagement:
> "$PNKSTR will keep rolling through all market types, its unlike any other narrative in crypto..."

---

## Technical Observations

### ✅ What Worked Well

1. **Authentication**: Seamless with Bearer Token
2. **Search Performance**: Fast response (~630ms per query)
3. **Data Quality**: Rich metadata including verified status, metrics, timestamps
4. **Rate Limits**: No issues hitting limits with 100 results/query

### ⚠️ Issues Encountered

**Cashtag Operator Not Available**
```
Error: Reference to invalid operator 'cashtag'
Query: "$PNKSTR"
```
- The `$` cashtag operator is not available in current PPU tier
- Had to search for plain text "PNKSTR" instead
- This limits ability to filter token-specific mentions vs general text

---

## API Usage

**Total Calls**: 2
- 1x search_recent_tweets (PNKSTR) → Success
- 1x search_recent_tweets ($PNKSTR) → Failed (cashtag operator)

**Cost**: TBD (checking console.x.com/billing)

---

## Use Case: Web3 + Social Intelligence

**Goal**: Correlate on-chain holder behavior with Twitter sentiment

We're analyzing PNSKTR (Punk Strategy token) holders from Nansen:
- 17,162 holders on Ethereum
- 96 "smart money" wallets
- Cross-referencing with Twitter to find:
  - Which whales are vocal vs silent
  - Sentiment trends before price moves
  - Bot vs genuine engagement

**Why This Matters for X API**:
- Novel crypto/Web3 use case
- Combines blockchain + social data
- PPU model perfect for research (bursty usage)

---

## Feature Requests

1. **Cashtag Support**: Enable `$TOKEN` operator for all tiers
   - Critical for crypto research
   - Helps filter out false positives

2. **Historical Search**: Access to tweets older than 7 days
   - Need to analyze token launch periods
   - Compare early vs current sentiment

3. **Bulk User Lookup**: Efficient batch lookup for wallet addresses
   - We have 198 smart money wallets to enrich
   - Need Twitter profiles for each

4. **ENS/Web3 Fields**: Add blockchain identifiers to user profiles
   - ENS names, wallet addresses in bio
   - Verified on-chain credentials

---

## Next Steps (Day 2)

- Sentiment scoring with NLP
- Wallet-to-Twitter enrichment (smart money tracker)
- Bot detection analysis
- Cost analysis report

---

## Files Generated

```
x-api-ppu-pilot/
├── data/pnsktr_tweets_20251120_115322.csv    (25KB, 100 tweets)
├── logs/api_calls_20251120_115322.txt        (363B, 2 calls)
└── day1_pnsktr_search.py                     (6.3KB, source code)
```

---

**Feedback Summary**: The X API v2 is fast and reliable for basic search. The missing cashtag operator is a blocker for crypto research. PPU pricing makes sense for our bursty research workflow vs fixed $200/month Pro tier.
