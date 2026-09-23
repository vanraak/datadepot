import pandas as pd

def load_diamonds() -> pd.DataFrame:
    try:
        import seaborn as sns
        return sns.load_dataset("diamonds")

    except Exception:
        import requests
        from io import BytesIO

        url = (
            "https://raw.githubusercontent.com/"
            "mwaskom/seaborn-data/master/diamonds.csv"
        )

        response = requests.get(url, timeout=30)
        response.raise_for_status()

        return pd.read_csv(BytesIO(response.content))