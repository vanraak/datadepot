import pandas as pd

from sklearn.compose import make_column_transformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from ..core import load


def prepare_online_shoppers_knn():
    df = load("online_shoppers")

    X = df.drop(columns="revenue")

    y = df["revenue"].map({True: 1, False: 0})

    cat_cols = [
        "month",
        "operating_systems",
        "browser",
        "region",
        "traffic_type",
        "visitor_type",
        "weekend",
    ]
    num_cols = [
        "administrative",
        "administrative_duration",
        "informational",
        "informational_duration",
        "product_related",
        "product_related_duration",
        "bounce_rates",
        "exit_rates",
        "page_values",
        "special_day",
    ]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.15,
        random_state=42,
        stratify=y,
    )

    ohe = OneHotEncoder(handle_unknown="ignore", sparse_output=False)

    scaler = StandardScaler()

    ct = make_column_transformer(
        (ohe, cat_cols),
        (scaler, num_cols),
        verbose_feature_names_out=False,
    )
    ct.set_output(transform="pandas")

    return X_train, X_test, y_train, y_test, ct
