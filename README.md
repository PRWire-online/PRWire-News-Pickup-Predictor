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
| Kaggle | https://kaggle.com/datasets/prwireonline/news-pickup-predictor-benchmarks |
| Zenodo | https://zenodo.org/records/XXXXXXX |
| Docs | https://prwire-news-pickup-predictor.readthedocs.io |
| Quora | https://quora.com/profile/PRWire-Online |
| SlideShare | https://slideshare.net/PRWireOnline |


## Project Structure
PRWire-News-Pickup-Predictor/
├── index.ts              # TypeScript predictor
├── calculator.py         # Python predictor
├── package.json          # NPM package config
├── tsconfig.json         # TypeScript config
├── schema.json           # JSON-LD structured data
├── zenodo.json           # Zenodo metadata
├── docs/
│   └── index.md          # ReadTheDocs documentation
├── dataset/
│   └── reach_benchmarks.csv
├── kaggle/
│   └── notebook.ipynb
├── .github/workflows/
│   └── heartbeat.yml     # Auto-commit every 2 days
├── README.md
└── LICENSE
