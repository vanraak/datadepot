import pandas as pd
from importlib.resources import files

DATASETS = {
    "adult": {
        "description": "Adult census income dataset.",
        "source": "UC Irvine Machine Learning Repository",
        "creators": "Barry Becker and Ronny Kohavi",
        "url": "https://archive.ics.uci.edu/dataset/2/adult",
        "license": "Creative Commons Attribution 4.0 International",
        "license_url": "https://creativecommons.org/licenses/by/4.0/",
    },
    "bank": {
        "description": "Bank marketing dataset.",
        "source": "UC Irvine Machine Learning Repository",
        "creators": "S. Moro, P. Rita and P. Cortez",
        "url": "https://archive.ics.uci.edu/ml/datasets/bank+marketing",
        "license": "Creative Commons Attribution 4.0 International",
        "license_url": "https://creativecommons.org/licenses/by/4.0/",
    },
    "bicycle_counts": {
        "description": "Daily total of bike counts for East River Bridges.",
        "source": "NYC OpenData",
        "creators": "NYC Department of Transportation (DOT)",
        "url": "https://data.cityofnewyork.us/Transportation/Bicycle-Counts-for-East-River-Bridges-Historical-/gua4-p9wg/about_data",
        "license": "New York City Open Data Terms of Use",
        "license_url": "https://data.cityofnewyork.us/stories/s/Terms-of-Use/k9k7-3cje/",
    },
    "bike_sharing": {
        "description": "Seoul Bike Sharing Demand dataset.",
        "source": "UC Irvine Machine Learning Repository",
        "creators": "Seoul Open Data Plaza",
        "url": "https://archive.ics.uci.edu/dataset/560/seoul+bike+sharing+demand",
        "license": "Creative Commons Attribution 4.0 International",
        "license_url": "https://creativecommons.org/licenses/by/4.0/",
    },
    "churn": {
        "description": "Credit card churn dataset.",
        "source": "Kaggle",
        "creators": "Sakshi Goyal (Kaggle contributor)",
        "url": "https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers",
        "license": "CC0: Public Domain",
        "license_url": "https://creativecommons.org/publicdomain/zero/1.0/",
    },
    "cpu": {
        "description": "Dataset of CPU pricing and performance characteristics.",
        "source": "datadepot",
        "creators": "Jeroen van Raak (data compilation)",
        "url": "https://github.com/vanraak/datadepot",
        "license": "CC BY 4.0",
        "license_url": "http://creativecommons.org/licenses/by/4.0/",
    },
    "credit": {
        "description": "700 good and 300 bad credits with 20 predictor variables. Data from 1973 to 1975.",
        "source": "UC Irvine Machine Learning Repository",
        "creators": "Hans Hofmann",
        "url": "https://doi.org/10.24432/C5QG88",
        "license": "CC BY 4.0",
        "license_url": "https://creativecommons.org/licenses/by/4.0/",
    },
    "credit_card": {
        "description": "Anonymized credit card transactions labeled as fraudulent or genuine",
        "source": "Kaggle",
        "creators": "Machine Learning Group - ULB",
        "url": "https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud",
        "license": "Database Contents License (DbCL) v1.0",
        "license_url": "http://opendatacommons.org/licenses/dbcl/1.0/",
    },
    "diamonds": {
        "description": "Diamonds dataset",
        "source": "ggplot2 package",
        "creators": "Loose Diamonds Search Engine",
        "url": "https://ggplot2.tidyverse.org/reference/diamonds.html",
        "license": "MIT",
        "license_url": "https://ggplot2.tidyverse.org/LICENSE.html",
        "citation": "Wickham H (2016). ggplot2: Elegant Graphics for Data Analysis. Springer-Verlag New York. ISBN 978-3-319-24277-4",
    },
    "drug": {
        "description": "Drug classification dataset.",
        "source": "liver - R Package",
        "creators": "Reza Mohammadi",
        "url": "https://cran.r-project.org/web/packages/liver/",
        "license": "GPL-3",
        "license_url": "https://cran.r-project.org/web/licenses/GPL-3",
    },
    "house": {
        "description": "Real Estate Valuation",
        "source": "UC Irvine Machine Learning Repository",
        "creators": "I-Cheng Yeh",
        "url": "https://archive.ics.uci.edu/dataset/477/real+estate+valuation+data+set",
        "license": "CC BY 4.0",
        "license_url": "https://creativecommons.org/licenses/by/4.0/",
    },
    "house_price": {
        "description": "House price dataset.",
        "source": "Kaggle",
        "creators": "Dean De Cock",
        "url": "https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data",
        "license": "MIT",
        "license_url": "https://www.mit.edu/~amini/LICENSE.md",
    },
    "loan": {
        "description": "The loan approval dataset is a collection of financial records and associated information used to determine the eligibility of individuals or organizations for obtaining loans from a lending institution.",
        "source": "Kaggle",
        "creators": "Archit Sharma (Kaggle contributor)",
        "url": "https://www.kaggle.com/datasets/architsharma01/loan-approval-prediction-dataset",
        "license": "MIT",
        "license_url": "https://www.mit.edu/~amini/LICENSE.md",
    },
    "mpg": {
        "description": "Auto MPG dataset.",
        "source": "UC Irvine Machine Learning Repository",
        "creators": "R. Quinlan",
        "url": "https://archive.ics.uci.edu/ml/datasets/auto+mpg",
        "license": "CC BY 4.0",
        "license_url": "https://creativecommons.org/licenses/by/4.0/",
    },
    "nyc_taxi": {
        "description": "NYC Yellow Taxi Zones dataset.",
        "source": "NYC TLC Trip Record Data",
        "creators": "NYC Taxi & Limousine Commission",
        "url": "https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page",
        "license": "NYC.gov Terms of Use",
        "license_url": "https://www.nyc.gov/main/terms-of-use",
    },
    "online_shoppers": {
        "description": "Online Shoppers Purchasing Intention dataset.",
        "source": "UC Irvine Machine Learning Repository",
        "creators": "C. Sakar and Y. Kastro",
        "url": "https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset",
        "license": "CC BY 4.0",
        "license_url": "https://creativecommons.org/licenses/by/4.0/",
    },
    "red_wines": {
        "description": "Red wine quality dataset.",
        "source": "UC Irvine Machine Learning Repository",
        "creators": "Paulo Cortez, António Cerdeira, Fernando Almeida, Telmo Matos, and José Reis",
        "url": "https://archive.ics.uci.edu/ml/datasets/wine+quality",
        "license": "CC BY 4.0",
        "license_url": "https://creativecommons.org/licenses/by/4.0/",
    },
}


def _normalize(name: str) -> str:
    """Normalize dataset names for flexible lookup."""
    return name.strip().lower().replace("_", "").replace("-", "")


def _lookup_name(name: str) -> str:
    """Return canonical dataset name."""
    lookup = {k.replace("_", ""): k for k in DATASETS}
    key = _normalize(name)

    if key not in lookup:
        raise ValueError(f"Dataset '{name}' does not exist.")

    return lookup[key]


def load(name: str) -> pd.DataFrame:
    """Load a dataset as a pandas DataFrame."""

    if _normalize(name) in ["mnist", "fashionmnist", "fashion"]:
        raise RuntimeError(
            f"Dataset '{name}' is not included in datadepot. "
            "Please load this dataset using tensorflow.keras instead."
        )

    canonical_name = _lookup_name(name)

    try:
        csv_file = files("datadepot.data").joinpath(f"{canonical_name}.csv.gz")
        return pd.read_csv(csv_file, sep=",", encoding="utf-8", compression="gzip")
    except Exception as e:
        raise RuntimeError(f"Failed to load dataset '{canonical_name}': {e}")


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
    print(f"{'License':<{width}}: {meta.get('license','')}")
    print(f"{'License URL':<{width}}: {meta.get('license_url','')}")
    print(line)


def dataset_table() -> str:
    """Generate a dynamic-width table of datasets."""
    name_width = max(len(name) for name in DATASETS) + 2
    desc_width = max(len(d["description"]) for d in DATASETS.values()) + 2

    table_lines = [
        f"{'Dataset':<{name_width}} {'Description':<{desc_width}}",
        "-" * (name_width + desc_width),
    ]

    for name, meta in DATASETS.items():
        table_lines.append(f"{name:<{name_width}} {meta['description']:<{desc_width}}")

    return "\n".join(table_lines)


def list_datasets():
    return list(DATASETS.keys())


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
