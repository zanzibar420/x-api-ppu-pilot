# X API PPU Pilot - Day 1: XDK vs Tweepy Comparison

**Date**: November 20, 2025
**Tester**: @ZanzibarVenturz
**Project**: Token Community Intelligence Platform

---

## Summary

We tested **both** third-party library (Tweepy) and the **official Python XDK** for the same PNSKTR search task.

---

## Results Comparison

### Tweepy (Third-Party)
- **API Calls**: 2
- **Results**: 100 tweets from "PNKSTR" query
- **Setup Time**: ~5 minutes
- **Code Complexity**: Moderate
- **Documentation**: Excellent (mature library)

### Official XDK
- **API Calls**: 1 (more efficient!)
- **Results**: 100 tweets from "PNKSTR" query
- **Setup Time**: ~15 minutes (learning curve)
- **Code Complexity**: Simple once understood
- **Documentation**: Needs improvement

---

## XDK Experience (The Good)

### ✅ Pros

1. **Simpler Authentication**
   ```python
   # Just one line!
   client = Client(bearer_token=BEARER_TOKEN)
   ```

2. **Cleaner API**
   ```python
   response = client.posts.search_recent(query='PNKSTR', max_results=100)
   ```

3. **First-Party Support**
   - Official support from X team
   - Will get updates first
   - Built for the future

4. **Pydantic Models**
   - Response is typed (SearchRecentResponse)
   - Helps with IDE autocomplete

---

## XDK Experience (The Challenges)

### ⚠️ Pain Points

1. **Parameter Naming Confusion**
   - Expected: `tweet_fields`, `user_fields` (like X API docs)
   - Actual: `tweetfields`, `userfields` (no underscore, all lowercase)
   - This caused initial errors

2. **Mixed Data Types**
   - Response is Pydantic model (`SearchRecentResponse`)
   - But `response.data` contains plain `dict` objects
   - Expected consistent object models throughout

3. **Limited Documentation**
   - No examples in PyPI page
   - Had to use `help()` and `dir()` to discover API
   - Naming conventions not documented

4. **Import Structure**
   - Initially tried: `from xdk.auth import BearerToken`
   - Actual: Authentication params passed directly to `Client()`
   - Not intuitive from announcement post

---

## Code Comparison

### Tweepy (16 lines)
```python
import tweepy

client = tweepy.Client(bearer_token=BEARER_TOKEN)

response = client.search_recent_tweets(
    query='PNKSTR',
    max_results=100,
    tweet_fields=['created_at', 'public_metrics'],
    expansions=['author_id'],
    user_fields=['username', 'name']
)

for tweet in response.data:
    print(tweet.id, tweet.text)  # Objects with attributes
```

### Official XDK (16 lines)
```python
from xdk import Client

client = Client(bearer_token=BEARER_TOKEN)

response = client.posts.search_recent(
    query='PNKSTR',
    max_results=100,
    tweetfields=['created_at', 'public_metrics'],  # lowercase!
    expansions=['author_id'],
    userfields=['username', 'name']  # lowercase!
)

for tweet in response.data:
    print(tweet['id'], tweet['text'])  # Dicts, not objects
```

---

## Recommendations for X Team

### High Priority

1. **Update Documentation**
   - Add parameter naming guide (tweetfields vs tweet_fields)
   - Include complete code examples
   - Document dict vs object returns

2. **Consistent Data Models**
   - Either make `response.data` return Pydantic models too
   - Or document why mixing dict/object is beneficial

3. **Better Error Messages**
   - When `tweet_fields` is used, suggest `tweetfields`
   - Help developers migrate from Tweepy

### Medium Priority

4. **Add Type Hints**
   - `SearchRecentResponse.data: List[Dict]` should be typed
   - Helps with IDE autocomplete

5. **Examples Repository**
   - Common patterns (search, users, streaming)
   - Migration guide from Tweepy

---

## Performance Notes

**Tweepy**: 2 API calls, ~1.2 seconds total
**XDK**: 1 API call, ~0.6 seconds total

XDK was **faster** and more **efficient** (fewer API calls for same task).

---

## Will We Use XDK Going Forward?

**Yes!** Despite the learning curve, the official XDK is:
- Faster
- More efficient
- First-party supported
- Future-proof

We'll continue building with XDK and provide ongoing feedback to improve developer experience.

---

## API Usage Cost

**Total calls today**: 3 (2 Tweepy + 1 XDK)
**Tweets retrieved**: 200
**User lookups**: ~200 (via expansions)

**Awaiting**: PPU cost breakdown from console.x.com

---

## Files Generated

```
x-api-ppu-pilot/
├── day1_pnsktr_search.py           # Tweepy version
├── day1_pnsktr_search_xdk.py       # Official XDK version ✅
├── data/
│   ├── pnsktr_tweets_20251120_115322.csv    # Tweepy results
│   └── pnsktr_tweets_xdk_20251120_122206.csv # XDK results
└── logs/
    ├── api_calls_20251120_115322.txt         # Tweepy log
    └── xdk_api_calls_20251120_122206.txt     # XDK log
```

---

**Bottom Line**: XDK is the future, but needs better docs. We're committed to using it and providing feedback to improve the developer experience.
