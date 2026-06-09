# PRWire News Pickup Predictor

Predict press release news pickup probability and estimated syndication reach. Built by [PRWire.online](https://prwire.online) powered by BHMarketer.

## Features

- Estimate pickup probability for press releases (0–100 score)
- Syndication reach estimator across wire outlets
- CLI support in Node.js and Python
- Benchmark dataset included (20 press releases)
- Lightweight, publish-ready, minimal dependencies

## Quick Start

### Node.js

```bash
npm install @prwire-online/news-pickup-predictor
npx news-pickup-predictor 50 global
```

### Python

```bash
pip install prwire-news-pickup-predictor
python -m predictor 50 global
```

## Links

| Platform | URL |
|----------|-----|
| Website | https://prwire.online |
| GitHub | https://github.com/PRWire-online/PRWire-News-Pickup-Predictor |
| NPM | https://npmjs.com/package/@prwire-online/news-pickup-predictor |
| Hugging Face | https://huggingface.co/datasets/PRWire-online/prwire-news-pickup-benchmarks |
| Kaggle | https://kaggle.com/datasets/prwireonline1/news-pickup-predictor-benchmarks |
| Zenodo | https://zenodo.org/records/XXXXXXX |
| Docs | https://prwire-news-pickup-predictor.readthedocs.io |
| Quora | https://quora.com/profile/PRWire-Online |
| SlideShare | https://slideshare.net/PRWireOnline |

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
