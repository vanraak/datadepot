import pandas as pd
from ucimlrepo import fetch_ucirepo


def load_red_wines() -> pd.DataFrame:
    try:
        wine_quality = fetch_ucirepo(id=186)
        df = wine_quality.data.original.copy()
    except:
        from io import BytesIO
        import requests
        
        url = "https://archive.ics.uci.edu/static/public/186/data.csv"

        r = requests.get(url, timeout=30)
        r.raise_for_status()

        df = pd.read_csv(BytesIO(r.content))

    df = df.loc[df["color"] == "red"].drop(columns="color")

    return df
