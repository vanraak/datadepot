import pandas as pd
import warnings

with warnings.catch_warnings():
    warnings.filterwarnings(
        "ignore",
        message="IProgress not found.*",
    )

    from huggingface_hub import hf_hub_download
    from huggingface_hub.utils import (
        are_progress_bars_disabled,
        disable_progress_bars,
        enable_progress_bars,
    )


def _hf_download(**kwargs) -> str:
    was_disabled = are_progress_bars_disabled()

    if not was_disabled:
        disable_progress_bars()

    try:
        return hf_hub_download(**kwargs)
    finally:
        if not was_disabled:
            enable_progress_bars()


def load_imdb() -> tuple[pd.DataFrame, pd.DataFrame]:
    files = {
        "train": "plain_text/train-00000-of-00001.parquet",
        "test": "plain_text/test-00000-of-00001.parquet",
    }

    frames = {}

    for split, filename in files.items():
        path = _hf_download(
            repo_id="stanfordnlp/imdb",
            repo_type="dataset",
            revision="e6281661ce1c48d982bc483cf8a173c1bbeb5d31",
            filename=filename,
        )

        frames[split] = pd.read_parquet(path)

    return frames["train"], frames["test"]
