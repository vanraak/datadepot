import pandas as pd
from ucimlrepo import fetch_ucirepo


def load_bike_sharing() -> pd.DataFrame:
    bike_sharing = fetch_ucirepo(id=560)
    df = bike_sharing.data.original.copy()

    df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")
    df = df.rename(
        columns={
            "rented_bike_count": "bike_count",
        }
    )

    return df
