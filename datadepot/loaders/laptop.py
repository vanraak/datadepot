import pandas as pd
from importlib.resources import files

def load_laptop() -> pd.DataFrame:
    path = files("datadepot.data").joinpath(f"laptop.csv.gz")

    return pd.read_csv(
        path,
        sep=",",
        encoding="utf-8",
        compression="gzip",
    )
