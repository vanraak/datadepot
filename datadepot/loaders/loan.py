from ._kaggle import kagglehub
import pandas as pd


def load_loan() -> pd.DataFrame:
    path = kagglehub.dataset_download(
        "architsharma01/loan-approval-prediction-dataset",
        path="loan_approval_dataset.csv",
    )

    df = pd.read_csv(path)

    return df
