# X API Pay-Per-Use Pilot: PNSKTR Intelligence

**Tester:** [@ZanzibarVenturz](https://x.com/ZanzibarVenturz)
**Project:** Token Community Intelligence Platform
**Status:** Day 1 - Active Development

---

## Overview

Testing the new **X API Pay-Per-Use (PPU)** model and **official Python XDK** for crypto token community analysis. This project tracks Twitter sentiment, engagement, and influencer activity for **PNSKTR** (Punk Strategy token).

### Why This Matters

Traditional $200/month Pro tier is expensive for research use cases with variable usage. PPU model allows:
- Pay only for what you use
- Perfect for bursty research workflows
- Better economics for crypto/web3 projects

---

## Day 1 Results

### API Usage
- **Queries**: 1 search
- **Tweets Retrieved**: 100
- **Cost**: $0.50
- **Economics**: **93% cheaper** than Pro tier for our use case

### Technical Stack
- ✅ Official Python XDK (0.2.2b0)
- ✅ Bearer Token authentication
- ✅ CSV export for analysis
- ✅ API call logging for cost tracking

### Key Findings

**PNSKTR Twitter Activity (Nov 19-20):**
- 100 tweets over 17 hours
- 85% bullish sentiment
- Top topic: Token burns (51k PNSKTR/day)
- Average engagement: 5.1 retweets, 3.8 likes
- 73% retweets vs original content

**Top Influencers:**
- @ApeNuke (1.3K impressions)
- @BastionVonRaven (burn announcements)
- @reesistancee (market cap updates)

---

## Project Structure

```
x-api-ppu-pilot/
├── day1_pnsktr_search_xdk.py    # Official XDK implementation
├── day1_pnsktr_search.py        # Tweepy comparison
├── requirements.txt              # Python dependencies
├── .env.example                  # Template for credentials
├── data/                         # Tweet exports (CSVs)
├── logs/                         # API call tracking
├── DAY_1_PILOT_FEEDBACK.md      # Feedback for X team
└── DAY_1_XDK_COMPARISON.md      # XDK vs Tweepy analysis
```

---

## Setup

### 1. Get PPU Pilot Access
1. Apply for X API PPU pilot
2. Create new app at [console.x.com](https://console.x.com)
3. Copy Bearer Token

### 2. Install Dependencies

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install packages
pip install -r requirements.txt
```

### 3. Configure Credentials

```bash
# Copy template
cp .env.example .env

# Edit .env and add your credentials
TWITTER_BEARER_TOKEN=your_bearer_token_here
```

### 4. Run Day 1 Script

```bash
python day1_pnsktr_search_xdk.py
```

**Output:**
- CSV: `data/pnsktr_tweets_xdk_YYYYMMDD_HHMMSS.csv`
- Log: `logs/xdk_api_calls_YYYYMMDD_HHMMSS.txt`

---

## XDK Experience

### ✅ Pros
- Simple authentication: `Client(bearer_token=TOKEN)`
- Fast response times (~600ms)
- Official first-party support
- Future-proof

### ⚠️ Challenges
- Parameter naming confusion (`tweetfields` not `tweet_fields`)
- Mixed dict/object response types
- Sparse documentation
- Learning curve from Tweepy

**Full comparison:** [DAY_1_XDK_COMPARISON.md](DAY_1_XDK_COMPARISON.md)

---

## Cost Analysis

### PPU Pricing (Actual)
```
$0.50 per search_recent call (100 tweets + user expansions)
```

### Budget Projections

**$500 Credit Gets You:**
- 1,000 search queries
- 100,000 tweets analyzed
- ~6 months of daily monitoring

**vs Pro Tier:**
- Pro: $200/month fixed
- PPU: ~$15/month for our usage
- **Savings: 93%**

---

## Pilot Feedback Summary

### For X Team

**What Works:**
✅ PPU model perfect for research use cases
✅ XDK authentication is simple
✅ Performance is excellent

**Needs Improvement:**
⚠️ Parameter naming should match API docs
⚠️ Add more code examples for XDK
⚠️ Document dict vs object returns

**Feature Requests:**
- Enable cashtag operator (`$TOKEN`) in PPU tier
- Historical search beyond 7 days
- Bulk user lookup for wallet enrichment
- Web3/ENS fields in user profiles

**Full feedback:** [DAY_1_PILOT_FEEDBACK.md](DAY_1_PILOT_FEEDBACK.md)

---

## Use Case: Web3 + Social Intelligence

This pilot demonstrates **unique crypto/web3 value**:

1. **Token Community Health** - Track sentiment, influencer activity, bot detection
2. **Smart Money Intelligence** - Cross-reference on-chain wallets with Twitter accounts
3. **Holder Engagement** - Measure community conviction vs price action
4. **Early Alpha Detection** - Identify accumulation signals before price moves

**Data Sources Combined:**
- X API (social sentiment)
- Nansen (smart money labels)
- On-chain data (wallet balances, transactions)

---

## Roadmap

### Week 1
- [x] Day 1: Basic search & XDK testing
- [ ] Day 2: Sentiment scoring with NLP
- [ ] Day 3: Smart money wallet enrichment
- [ ] Day 4: Bot detection analysis

### Week 2+
- [ ] Real-time monitoring with filtered stream
- [ ] Automated daily reports
- [ ] Expand to other TokenWorks strategies
- [ ] Build Web3 ↔ Social correlation engine

---

## Contributing

This is a pilot project - feedback welcome!

- Found a bug? Open an issue
- Have suggestions? Submit a PR
- Using PPU yourself? Share your experience

---

## License

MIT License - Feel free to fork and build upon this!

---

## Links

- **X API Docs:** https://developer.x.com
- **XDK GitHub:** https://github.com/xdevplatform
- **PNSKTR Token:** [0xc50673edb3a7b94e8cad8a7d4e0cd68864e33edf](https://etherscan.io/address/0xc50673edb3a7b94e8cad8a7d4e0cd68864e33edf)
- **Nansen:** https://app.nansen.ai/token-god-mode?tokenAddress=0xc50673edb3a7b94e8cad8a7d4e0cd68864e33edf

---

**Built with the X API Pay-Per-Use pilot | November 2025**
