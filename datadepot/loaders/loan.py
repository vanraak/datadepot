from ._kaggle import kagglehub
import pandas as pd


def load_loan() -> pd.DataFrame:
    path = kagglehub.dataset_download(
        "architsharma01/loan-approval-prediction-dataset",
        path="loan_approval_dataset.csv",
    )

    df = pd.read_csv(path)

    df.columns = df.columns.str.strip()

    df["loan_status"] = df["loan_status"].str.strip()
    df["education"] = df["education"].str.strip()
    df["self_employed"] = df["self_employed"].str.strip()

    return df
