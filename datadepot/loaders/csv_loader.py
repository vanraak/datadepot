from importlib.resources import files
import pandas as pd


def load(meta: dict, canonical_name: str) -> pd.DataFrame:
    path = files("datadepot.data").joinpath(f"{canonical_name}.csv.gz")

    return pd.read_csv(
        path,
        sep=",",
        encoding="utf-8",
        compression="gzip",
    )
