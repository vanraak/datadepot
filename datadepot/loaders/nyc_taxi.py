import pandas as pd
from importlib.resources import files


def load_nyc_taxi() -> pd.DataFrame:
    path = files("datadepot.data").joinpath(f"nyc_taxi.csv.gz")

    return pd.read_csv(
        path,
        sep=",",
        encoding="utf-8",
        compression="gzip",
    )
