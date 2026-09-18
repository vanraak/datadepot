import pandas as pd
from ucimlrepo import fetch_ucirepo


def load_online_shoppers() -> pd.DataFrame:
    online_shoppers = fetch_ucirepo(id=468)
    df = online_shoppers.data.original.copy()

    df.columns = (
        df.columns.str.strip()
        .str.replace(r"([a-z0-9])([A-Z])", r"\1_\2", regex=True)
        .str.replace("-", "_")
        .str.lower()
    )

    return df
