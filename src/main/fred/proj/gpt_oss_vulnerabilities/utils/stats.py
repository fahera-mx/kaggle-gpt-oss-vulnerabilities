import pandas as pd
import numpy as np


def get_absolute_odds(
        df: pd.DataFrame,
        col_category: str,
        col_target: str,
):
    return (
        df.query(f"{col_target} == 1")
        .groupby(col_category, as_index=False).size().rename(columns={"size": 1})
        .set_index(col_category)
    ).join(
        df.query(f"{col_target} == 0")
        .groupby(col_category, as_index=False).size().rename(columns={"size": 0})
        .set_index(col_category)
    ).reset_index()


def get_relative_odds(
        df: pd.DataFrame,
        col_category: str,
        col_target: str,
):
    odds = get_absolute_odds(df, col_category, col_target)
    totals = {
        key: odds[key].sum()
        for key in [0, 1]
    }

    return odds.apply(
        lambda row: pd.Series({
            **row.to_dict(),
            1: row[1] / totals[1] if totals[1] > 0 else np.nan,
            0: row[0] / totals[0] if totals[0] > 0 else np.nan,
        }),
        axis=1
    )