import pandas as pd
from ucimlrepo import fetch_ucirepo


def load_bank() -> pd.DataFrame:
    try:
        bank_marketing = fetch_ucirepo(id=222)
        df = bank_marketing.data.original.copy()

    except Exception:
        from io import BytesIO
        import requests
        
        url = "https://archive.ics.uci.edu/static/public/222/data.csv"

        r = requests.get(url, timeout=30)
        r.raise_for_status()

        df = pd.read_csv(BytesIO(r.content))

    df.columns = df.columns.str.lower().str.strip().str.replace("-", "_")
    df = df.fillna("unknown")
    df = df.rename(columns={"y": "deposit",
                            "day_of_week": "day"})

    return df
