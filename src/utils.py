"""Shared utilities for the Allstate Claims Severity project."""

import os
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Paths — all relative to the project root
# ---------------------------------------------------------------------------
DATA_RAW    = "data/raw/"
DATA_CLEAN  = "data/cleansing/"
SUBMISSIONS = "data/submissions-kaggle/"
REPORTS     = "reports/images/"

TRAIN_RAW   = DATA_RAW    + "train.csv"
TEST_RAW    = DATA_RAW    + "test.csv"
SAMPLE_SUB  = DATA_RAW    + "sample_submission.csv"
TRAIN_CLEAN = DATA_CLEAN  + "train.csv"
TEST_CLEAN  = DATA_CLEAN  + "test.csv"

# ---------------------------------------------------------------------------
# Reproducibility
# ---------------------------------------------------------------------------
RANDOM_STATE = 42

# ---------------------------------------------------------------------------
# Modelling
# ---------------------------------------------------------------------------
# Shift applied before log-transform of the target to keep values > 0.
# loss_min ≈ 0.67; shift=200 guarantees log(loss + shift) is well-defined
# and reduces skew without distorting the distribution.
SHIFT = 200
N_FOLDS = 5


# ---------------------------------------------------------------------------
# Data helpers
# ---------------------------------------------------------------------------
def get_col(df: pd.DataFrame, type_descr) -> list:
    """Return column names matching *type_descr* (np.number, np.object, or list)."""
    try:
        cols = df.describe(include=type_descr).columns
    except ValueError:
        print(f"Dataframe contains no {type_descr} columns.")
        return []
    return cols.tolist()


def save_csv(df: pd.DataFrame, path: str) -> None:
    """Save *df* to *path* as UTF-8 CSV without the row index."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8")


def save_predictions(ids, predictions, path: str) -> None:
    """Write a Kaggle-style submission CSV (id, loss) to *path*."""
    submission = pd.DataFrame({"id": ids, "loss": predictions})
    save_csv(submission, path)


# ---------------------------------------------------------------------------
# Feature-selection helpers
# ---------------------------------------------------------------------------
def get_low_target_correlation(
    df: pd.DataFrame,
    feature_cols: list,
    target_col: str,
    threshold: float = 0.1,
) -> list:
    """
    Return feature columns whose absolute Pearson correlation with *target_col*
    is below *threshold*.  Prints the correlation table.
    """
    corr = df[feature_cols].corrwith(df[target_col]).abs().sort_values()
    low = corr[corr < threshold]
    print(f"{'─'*25} LOW TARGET CORRELATION (< {threshold}) {'─'*25}\n")
    print(low.to_string())
    print()
    return low.index.tolist()


def drop_columns(df: pd.DataFrame, cols: list, label: str = "") -> pd.DataFrame:
    """Drop *cols* from *df* and print before/after column counts."""
    before = df.shape[1]
    df = df.drop(columns=cols, errors="ignore")
    after = df.shape[1]
    tag = f"[{label}] " if label else ""
    print(f"{tag}Columns: {before} → {after}  (removed {before - after})")
    return df
