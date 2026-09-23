import pandas as pd
from ucimlrepo import fetch_ucirepo


def load_online_shoppers() -> pd.DataFrame:
    try:
        online_shoppers = fetch_ucirepo(id=468)
        df = online_shoppers.data.original.copy()

    except Exception:
        from io import BytesIO
        import requests
        
        url = "https://archive.ics.uci.edu/static/public/468/data.csv"

        r = requests.get(url, timeout=30)
        r.raise_for_status()

        df = pd.read_csv(BytesIO(r.content))

    df.columns = (
        df.columns.str.strip()
        .str.replace(r"([a-z0-9])([A-Z])", r"\1_\2", regex=True)
        .str.replace("-", "_")
        .str.lower()
    )

    return df
