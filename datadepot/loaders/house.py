import pandas as pd
from ucimlrepo import fetch_ucirepo


def load_house() -> pd.DataFrame:
    try:
        real_estate_valuation = fetch_ucirepo(id=477)
        df = real_estate_valuation.data.original.copy()

    except Exception:
        from io import BytesIO
        import requests
        
        url = "https://archive.ics.uci.edu/static/public/477/data.csv"

        r = requests.get(url, timeout=30)
        r.raise_for_status()

        df = pd.read_csv(BytesIO(r.content))

    df = df.rename(
        columns={
            "X2 house age": "house_age",
            "X3 distance to the nearest MRT station": "distance_to_mrt",
            "X4 number of convenience stores": "stores_number",
            "X5 latitude": "latitude",
            "X6 longitude": "longitude",
            "Y house price of unit area": "unit_price",
        }
    )

    columns = [
        "house_age",
        "distance_to_mrt",
        "stores_number",
        "latitude",
        "longitude",
        "unit_price",
    ]

    return df.loc[:, columns]
