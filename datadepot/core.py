import pandas as pd
from importlib.resources import files
from .registry import DATASETS
from .loaders import get_loader


def load(name: str) -> pd.DataFrame:

    canonical_name = _lookup_name(name)
    meta = DATASETS[canonical_name]

    loader = get_loader(meta["loader"])

    return loader(meta, canonical_name)


def info(name: str, return_dict: bool = False) -> dict | None:
    """
    Display detailed information about a dataset.

    Parameters
    ----------
    name : str
        Name of the dataset.
    return_dict : bool, default=False
        If True, return the metadata dictionary instead of printing it.

    Returns
    -------
    dict or None
        Dataset metadata if return_dict=True, otherwise None.
    """

    canonical_name = _lookup_name(name)
    meta = DATASETS[canonical_name]

    info_dict = {"name": canonical_name, **meta}

    if return_dict:
        return info_dict

    width = 12
    line = "-" * 60

    print(line)
    print(f"Dataset: {canonical_name}")
    print(line)
    print(f"{'Description':<{width}}: {meta.get('description','')}")
    print(f"{'Source':<{width}}: {meta.get('source','')}")
    print(f"{'URL':<{width}}: {meta.get('url','')}")
    print(f"{'Creators':<{width}}: {meta.get('creators','')}")
    if meta.get("loader") == "csv":
        hosted_by = "datadepot"
    else:
        hosted_by = meta.get("hosted_by", meta.get("loader", ""))
    print(f"{'Hosted by':<{width}}: {hosted_by}")
    print(f"{'License':<{width}}: {meta.get('license','')}")
    print(f"{'License URL':<{width}}: {meta.get('license_url','')}")
    print(line)


def dataset_table() -> str:
    """Return a dynamic-width table of datasets."""
    name_width = max(len(name) for name in DATASETS) + 2
    desc_width = max(len(d["description"]) for d in DATASETS.values()) + 2

    table_lines = [
        f"{'Dataset':<{name_width}} {'Description':<{desc_width}}",
        "-" * (name_width + desc_width),
    ]

    for name, meta in DATASETS.items():
        table_lines.append(
            f"{name:<{name_width}} {meta['description']:<{desc_width}}"
        )

    return "\n".join(table_lines)


def list_datasets():
    return list(DATASETS.keys())


def _normalize(name: str) -> str:
    return name.strip().lower().replace("_", "").replace("-", "")


def _lookup_name(name: str) -> str:
    lookup = {_normalize(k): k for k in DATASETS}

    key = _normalize(name)

    if key not in lookup:
        raise ValueError(f"Dataset '{name}' does not exist.")

    return lookup[key]


def load_zones():
    try:
        import geopandas as gpd
    except ImportError:
        raise ImportError(
            "load_zones() requires the optional dependency 'geopandas'. "
            "Please install geopandas before using this function."
        )

    path = files("datadepot").joinpath("data/taxi_zones.gpkg")

    return gpd.read_file(path)
