import pandas as pd
import pandas as pd
from huggingface_hub import hf_hub_download
from huggingface_hub.utils import (
    are_progress_bars_disabled,
    disable_progress_bars,
    enable_progress_bars,
)
from ._kaggle import kagglehub


def load_creditcard() -> pd.DataFrame:
    try:
        path = kagglehub.dataset_download(
            "mlg-ulb/creditcardfraud",
            path="creditcard.csv",
        )

    except Exception:
        path = _hf_download(
            repo_id="JEFFREY-VERDIERE/Creditcard",
            repo_type="dataset",
            filename="creditcard.csv",
        )

    df = pd.read_csv(path)

    df.columns = df.columns.str.lower().str.strip()
    df = df.rename(columns={"class": "fraud"})

    return df


