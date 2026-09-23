import pandas as pd
from ucimlrepo import fetch_ucirepo


def load_adult() -> pd.DataFrame:
    try:
        adult = fetch_ucirepo(id=2)
        df = adult.data.original.copy()

    except Exception:
        from io import BytesIO
        import requests
        
        url = "https://archive.ics.uci.edu/static/public/2/data.csv"

        r = requests.get(url, timeout=30)
        r.raise_for_status()

        df = pd.read_csv(BytesIO(r.content))

    df.columns = df.columns.str.lower().str.strip().str.replace("-", "_")

    df["income"] = df["income"].str.replace("<=50K.", "<=50K")
    df["income"] = df["income"].str.replace(">50K.", ">50K")

    return df
