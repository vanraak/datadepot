import pandas as pd
from ucimlrepo import fetch_ucirepo


def load_bank() -> pd.DataFrame:
    bank_marketing = fetch_ucirepo(id=222)
    df = bank_marketing.data.original.copy()

    df.columns = df.columns.str.lower().str.strip().str.replace("-", "_")
    df = df.fillna("unknown")
    df = df.rename(columns={"y": "deposit"})

    return df
