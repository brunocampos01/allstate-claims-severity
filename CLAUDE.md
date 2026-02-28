# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Udacity ML Engineer Nanodegree capstone project predicting insurance claim severity (the `loss` column) using supervised learning. Based on the [Kaggle Allstate Claims Severity competition](https://www.kaggle.com/c/allstate-claims-severity/data).

## Environment Setup

```bash
# Install pinned deps (hash-verified)
pip install --require-hashes -r requirements.txt

# LightGBM is not yet in the pinned file — install separately
pip install lightgbm

jupyter lab
```

Tested with Python 3.6.8 and Pip 21.2.4.

`requirements.in` is the source file for direct dependencies. To regenerate the hash-pinned `requirements.txt` after adding a package to `requirements.in`:
```bash
pip-compile --generate-hashes requirements.in
```

## Running the Project

Notebooks must be run sequentially:

1. `notebooks/1-data-exploration-and-data-cleaning.ipynb` — EDA, feature encoding, PCA, outputs cleaned CSVs to `data/cleansing/`
2. `notebooks/2-modeling-and-evaluation.ipynb` — model training, cross-validation, generates Kaggle submission files

## Architecture & Data Flow

**Data directories:**
- `data/raw/` — original Kaggle CSVs (train.csv: 188,318 rows × 132 cols, test.csv: 125,546 rows × 131 cols)
- `data/cleansing/` — preprocessed data output by Notebook 1
- `data/submissions-kaggle/` — model prediction outputs per model, plus `ensemble_submission.csv`
- `models/` — persisted model files saved by joblib (created on first NB2 run)

**Shared constants & helpers:** `src/utils.py` — path constants (`DATA_RAW`, `DATA_CLEAN`, `SUBMISSIONS`), `RANDOM_STATE=42`, `SHIFT=200`, `N_FOLDS=5`, and helper functions (`get_col`, `save_csv`, `save_predictions`, `get_low_target_correlation`, `drop_columns`). Both notebooks import from this module.

**Feature space:** 116 categorical features (`cat1`–`cat116`) + 14 continuous features (`cont1`–`cont14`) → target: `loss`

**ML pipeline (Notebook 2):**
- Log transform with shift=200 applied to target `loss` before training (shift documented in `src/utils.py`)
- 5-fold cross-validation for all models, consistent `KFold(shuffle=True, random_state=42)`
- Four model families: Linear Regression (baseline), Random Forest, XGBoost, LightGBM
- Ensembling: weighted average (45% XGB + 45% LGBM + 10% RF) saved as `ensemble_submission.csv`
- Evaluation metric: MAE on inverse-transformed predictions
- Best single model: XGBoost MAE ~1135.90 (Kaggle benchmark ~1109.71)

**Reports & visualizations:** `reports/images/` contains 24 PNG plots (distributions, correlation matrices, PCA, model comparisons)
