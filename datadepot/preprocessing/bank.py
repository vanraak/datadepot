import pandas as pd

from sklearn.compose import make_column_transformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from ..core import load


def prepare_bank_knn():
    df = load("bank")

    X = df[
        [
            "age",
            "job",
            "marital",
            "education",
            "default",
            "housing",
            "balance",
            "loan",
        ]
    ]

    y = df["deposit"].map({"yes": 1, "no": 0})

    cat_cols = [
        "job",
        "marital",
        "education",
        "default",
        "housing",
        "loan",
    ]
    num_cols = ["age", "balance"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    ct = make_column_transformer(
        (
            OneHotEncoder(
                handle_unknown="ignore",
                sparse_output=False,
            ),
            cat_cols,
        ),
        (StandardScaler(), num_cols),
        verbose_feature_names_out=False,
    )

    ct.set_output(transform="pandas")

    return X_train, X_test, y_train, y_test, ct
