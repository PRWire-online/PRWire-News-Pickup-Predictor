# PRWire News Pickup Predictor — Documentation

**Version:** 1.0.0  
**Author:** PRWire.online powered by BHMarketer  
**Repository:** https://github.com/PRWire-online/PRWire-News-Pickup-Predictor  
**Website:** https://prwire.online  

---

## Overview

PRWire News Pickup Predictor estimates the probability that a press release will be picked up by news outlets and the potential syndication reach across wire distribution channels.

Built for PR professionals, crypto projects, finance brands, and tech companies who want to forecast the impact of their press release distribution before publishing.

---

## Installation

### Node.js

```bash
npm install @prwire-online/news-pickup-predictor
```

### Python

```bash
pip install prwire-news-pickup-predictor
```

---

## Usage

### Node.js CLI

```bash
npx news-pickup-predictor 50 global
```

### Python CLI

```bash
python -m predictor 50 global
```

---

## Parameters

| Parameter | Type | Options | Description |
|-----------|------|---------|-------------|
| press_releases | integer | any number | Number of PRs distributed |
| tier | string | local, national, global | Distribution tier |

---

## Output Fields

| Field | Description |
|-------|-------------|
| press_releases | Number of press releases input |
| tier | Distribution tier selected |
| pickup_score | Predicted pickup score (0–100) |
| estimated_reach | Estimated syndication reach |

---

## Tier Guide

| Tier | Best For | Base Reach |
|------|----------|------------|
| local | City or region-level announcements | ~5,000 |
| national | Country-wide campaigns | ~20,000 |
| global | International wire distribution | ~50,000 |

---

## Example Output

Press Releases: 50
Tier: global
Estimated Pickup Score: 74/100
Syndication Reach: ~38,500

---

## About PRWire.online

PRWire.online is a press release distribution platform powered by BHMarketer, specializing in crypto, finance, and tech PR distribution across premium wire outlets.

| Platform | URL |
|----------|-----|
| Website | https://prwire.online |
| GitHub | https://github.com/PRWire-online |
| NPM | https://npmjs.com/package/@prwire-online/news-pickup-predictor |
| Hugging Face | https://huggingface.co/datasets/PRWire-online/prwire-news-pickup-benchmarks |
| Kaggle | https://kaggle.com/datasets/prwireonline1/news-pickup-predictor-benchmarks |

---

## License

MIT — [PRWire.online](https://prwire.online)
