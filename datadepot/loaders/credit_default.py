import pandas as pd
from ucimlrepo import fetch_ucirepo


def load_credit_default() -> pd.DataFrame:

    try:
        default_of_credit_card_clients = fetch_ucirepo(id=350)

        df_features = default_of_credit_card_clients.data.features
        df_y = default_of_credit_card_clients.data.targets

    except Exception:
        from io import BytesIO
        import requests
        
        url = "https://archive.ics.uci.edu/static/public/350/data.csv"

        r = requests.get(url, timeout=30)
        r.raise_for_status()

        df = pd.read_csv(BytesIO(r.content))

        df_features = df.drop(columns=["Y"])
        df_y = df[["Y"]]


    df = pd.concat([df_features, df_y], axis=1)

    marital_labels = {
        1: "married",
        2: "single",
    }

    education_labels = {
        1: "graduate school",
        2: "university",
        3: "high school",
    }

    df["X4"] = df["X4"].map(marital_labels).fillna("other")
    df["X3"] = df["X3"].map(education_labels).fillna("other")

    df = df[["X1", "X3", "X4", "X5", "X6", "X12", "X18", "Y"]]

    df = df.rename(
        columns={
            "X1": "credit_amount",
            "X3": "education",
            "X4": "marital_status",
            "X5": "age",
            "X6": "repayment_status",
            "X12": "bill_amount",
            "X18": "latest_payment_amount",
            "Y": "default",
        }
    )

    return df
