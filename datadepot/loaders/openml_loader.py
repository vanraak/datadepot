import pandas as pd


def load(meta: dict, canonical_name: str) -> pd.DataFrame:
    if canonical_name == "creditcard":
        return load_creditcard()

    raise ValueError(f"No OpenML loader implemented for '{canonical_name}'")


def load_creditcard() -> pd.DataFrame:
    from sklearn.datasets import fetch_openml

    X, y = fetch_openml(
        "creditcard",
        version=1,
        return_X_y=True,
        as_frame=True,
    )
    y = y.astype(int)
    df = X.assign(target=y)
    df.columns = [col.lower() for col in df.columns]
    df = df.rename(columns={"target": "class"})
    return df
