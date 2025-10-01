# AdSpend Regression Predictor — Ipsha Gautam

**Brief**: This repository presents a compact, business-focused demonstration of multivariate linear regression applied to advertising spend channels (TV, Radio, Social, Online, Outdoor) to forecast sales. The goal is to show how investments across channels translate into incremental revenue, and how to communicate those findings to non-technical stakeholders.

## Why this project is different
- The dataset is a realistic synthetic sample constructed to preserve real-world scale and noise properties common in marketing budgets.
- The notebook emphasizes *interpretability*: coefficients are framed as marginal returns per dollar spent, and a cost-function visualization is included to show how model error changes with coefficient adjustments — a practical way to explain model sensitivity to business audiences.
- Compact, professional structure: notebook + script + sample_data + outputs for immediate reproducibility.

## Files
- `notebooks/ad_spend_regression.ipynb` — worked example with explanations and plots.
- `scripts/ad_spend_regression.py` — runnable script to reproduce figures.
- `sample_data/ad_spend_data.csv` — synthetic dataset (realistic scale).
- `outputs/` — visualizations used in report and README.
- `requirements.txt` — Python dependencies.
- `LICENSE` — MIT License.

## How to run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the notebook: `jupyter notebook notebooks/ad_spend_regression.ipynb`
3. Or run the script: `python scripts/ad_spend_regression.py` (this will generate PNGs in `outputs/`)

## Business takeaways (short)
- Coefficients show which channels provide higher marginal returns per dollar; use this to prioritize budget reallocations.  
- Residual analysis reveals where simple linear models may underfit and where more advanced time-series or interaction models could be needed.

### Dataset
The advertising dataset in this project is **synthetically generated using Python’s NumPy library**. It simulates ad spend across TV, Radio, Social Media, Online, and Outdoor channels with corresponding sales values.  
