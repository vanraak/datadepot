import pandas as pd
from ucimlrepo import fetch_ucirepo


def load_red_wines() -> pd.DataFrame:
    wine_quality = fetch_ucirepo(id=186)
    df = wine_quality.data.original.copy()
    df = df.loc[df["color"] == "red"].drop(columns="color")

    return df
