import pandas as pd


def load(meta: dict, canonical_name: str) -> pd.DataFrame:
    if canonical_name == "diamonds":
        return load_diamonds()

    raise ValueError(f"No seaborn loader implemented for '{canonical_name}'")


def load_diamonds() -> pd.DataFrame:
    try:
        import seaborn as sns
    except ImportError:
        raise ImportError(
            "Loading the diamonds dataset requires the optional dependency 'seaborn'. "
            "Please install seaborn before using this dataset."
        )

    return sns.load_dataset("diamonds")
