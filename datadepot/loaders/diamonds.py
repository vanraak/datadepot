import pandas as pd


def load_diamonds() -> pd.DataFrame:
    try:
        import seaborn as sns
    except ImportError as exc:
        raise ImportError("Loading diamonds requires seaborn.") from exc

    return sns.load_dataset("diamonds")
