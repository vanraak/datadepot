import pandas as pd
from importlib.resources import files


def load_house_price() -> pd.DataFrame:
    path = files("datadepot.data").joinpath(f"house_price.csv.gz")

    return pd.read_csv(
        path,
        sep=",",
        encoding="utf-8",
        compression="gzip",
    )
