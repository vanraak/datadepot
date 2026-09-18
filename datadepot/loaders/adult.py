import pandas as pd
from ucimlrepo import fetch_ucirepo


def load_adult() -> pd.DataFrame:
    adult = fetch_ucirepo(id=2)
    df = adult.data.original.copy()

    df.columns = df.columns.str.lower().str.strip().str.replace("-", "_")

    return df
