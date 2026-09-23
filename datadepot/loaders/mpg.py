import pandas as pd


def load_mpg() -> pd.DataFrame:
    try:
        import seaborn as sns
        return sns.load_dataset("mpg")

    except Exception:
        import requests
        from io import BytesIO

        url = (
            "https://raw.githubusercontent.com/"
            "mwaskom/seaborn-data/master/mpg.csv"
        )

        response = requests.get(url, timeout=30)
        response.raise_for_status()

        return pd.read_csv(BytesIO(response.content))