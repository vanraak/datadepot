import pandas as pd
from ucimlrepo import fetch_ucirepo


def load_bike_sharing() -> pd.DataFrame:
    try:
        bike_sharing = fetch_ucirepo(id=560)
        df = bike_sharing.data.original.copy()

    except Exception:
        from io import BytesIO
        import requests
        
        url = "https://archive.ics.uci.edu/static/public/560/data.csv"

        r = requests.get(url, timeout=30)
        r.raise_for_status()

        df = pd.read_csv(BytesIO(r.content))

    df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")
    df["date"] = (
        pd.to_datetime(df["date"], format="%d/%m/%Y")
        .dt.strftime("%Y-%m-%d")
        .astype("string")
    )
    df = df.rename(
        columns={
            "rented_bike_count": "bike_count",
        }
    )

    return df
