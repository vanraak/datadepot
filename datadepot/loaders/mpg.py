import pandas as pd


def load_mpg() -> pd.DataFrame:
    try:
        import seaborn as sns
    except ImportError as exc:
        raise ImportError("Loading mpg requires seaborn.") from exc

    return sns.load_dataset("mpg")
