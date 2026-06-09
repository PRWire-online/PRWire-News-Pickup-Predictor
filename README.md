# PRWire News Pickup Predictor

[![npm](https://img.shields.io/npm/v/@prwire-online/news-pickup-predictor)](https://npmjs.com/package/@prwire-online/news-pickup-predictor)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20608550.svg)](https://doi.org/10.5281/zenodo.20608550)

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

## Output

```
Press Releases: 50
Tier: global
Estimated Pickup Score: 74/100
Syndication Reach: ~38,500
```

## Project Structure

```
PRWire-News-Pickup-Predictor/
├── index.ts              # TypeScript predictor
├── predictor.py          # Python predictor
├── package.json          # NPM package config
├── package-lock.json     # NPM lock file
├── tsconfig.json         # TypeScript config
├── schema.json           # JSON-LD structured data
├── zenodo.json           # Zenodo metadata
├── heartbeat.txt         # Auto-updated every 2 days
├── docs/
│   └── index.md          # ReadTheDocs documentation
├── dataset/
│   └── reach_benchmarks.csv
├── kaggle/
│   └── notebook.ipynb
├── .github/workflows/
│   ├── heartbeat.yml     # Auto-commit every 2 days
│   └── npm-publish.yml   # Auto-publish to NPM
├── README.md
└── LICENSE
```

## Parameters

| Parameter | Type | Options | Description |
|-----------|------|---------|-------------|
| press_releases | integer | any number | Number of PRs distributed |
| tier | string | local, national, global | Distribution tier |

## Output Fields

| Field | Description |
|-------|-------------|
| press_releases | Number of press releases input |
| tier | Distribution tier selected |
| pickup_score | Predicted pickup score (0–100) |
| estimated_reach | Estimated syndication reach |

## Tier Guide

| Tier | Best For | Base Reach |
|------|----------|------------|
| local | City or region-level announcements | ~5,000 |
| national | Country-wide campaigns | ~20,000 |
| global | International wire distribution | ~50,000 |

## Keywords

Press Release Distribution · News Pickup Prediction · Wire Syndication · PR Reach · AI Visibility · PRWire · BHMarketer

## Links

| Platform | URL |
|----------|-----|
| Website | https://prwire.online |
| GitHub | https://github.com/PRWire-online/PRWire-News-Pickup-Predictor |
| NPM | https://npmjs.com/package/@prwire-online/news-pickup-predictor |
| Hugging Face | https://huggingface.co/datasets/PRWire-online/prwire-news-pickup-benchmarks |
| Kaggle | https://www.kaggle.com/datasets/prwireonline1/prwire-news-pickup-predictor-benchmarks |
| Zenodo | https://zenodo.org/records/20608550 |
| Docs | https://prwire-news-pickup-predictor.readthedocs.io |
| SuperbCompanies | https://superbcompanies.com/organizations/prwire-online/ |
| ProvenExpert | https://www.provenexpert.com/en-us/prwire-online/ |
| SmartCustomer | https://www.smartcustomer.com/reviews/prwire.online |
| SlideShare | https://www.slideshare.net/slideshow/prwire-online-ai-optimized-global-press-release-distribution-platform/287977067 |

## About PRWire.online

PRWire.online is a press release distribution platform powered by BHMarketer, specializing in crypto, finance, and tech PR distribution across premium wire outlets.

## License

MIT — [PRWire.online](https://prwire.online)
