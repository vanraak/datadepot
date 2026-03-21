import pandas as pd
import importlib.resources

DATASETS = {
    "adult": {
        "description": "Adult census income dataset.",
        "source": "UCI Irvine Machine Learning Repository",
        "creators": "Barry Becker and Ronny Kohavi",
        "url": "https://archive.ics.uci.edu/dataset/2/adult",
        "license": "Creative Commons Attribution 4.0 International",
        "license_url": "https://creativecommons.org/licenses/by/4.0/legalcode",
    },
    "bank": {
        "description": "Bank marketing dataset.",
        "source": "UCI  Irvine Machine Learning Repository",
        "creators": "S. Moro, P. Rita and P. Cortez",
        "url": "https://archive.ics.uci.edu/ml/datasets/bank+marketing",
        "license": "Creative Commons Attribution 4.0 International",
        "license_url": "https://creativecommons.org/licenses/by/4.0/legalcode",
    },
    "cereal": {
        "description": "Breakfast Cereal Data",
        "source": "American Statistical Association",
        "creators": "1993 ASA Statistical Graphics Expositio",
        "url": "https://community.amstat.org/stat-computing/data-expo/data-expo-1993",
        "license": "unknown",
        "license_url": "unknown",
    },
    "churn": {
        "description": "Credit card churn dataset.",
        "source": "Kaggle",
        "creators": "Sakshi Goyal",
        "url": "https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers",
        "license": "CC0: Public Domain",
        "license_url": "https://creativecommons.org/publicdomain/zero/1.0/",
    },
    "churn_ibm": {
        "description": "Telecom churn dataset (IBM).",
        "source": "IBM Sample Data",
        "creators": "IBM",
        "url": "https://github.com/IBM/telco-customer-churn-on-icp4d",
        "license": "Apache 2.0",
        "license_url": "https://www.apache.org/licenses/LICENSE-2.0",
    },
    "churn_mlc": {
        "description": "Telecom churn dataset (MLC).",
        "source": "OpenML",
        "creators": "Lennart Purucker",
        "url": "https://openml.org/d/46915",
        "license": "MIT",
        "license_url": "https://www.mit.edu/~amini/LICENSE.md",
    },
    "covid": {
        "description": "COVID-19 related dataset.",
        "source": "European Centre for Disease Prevention and Control",
        "creators": "European Centre for Disease Prevention and Control",
        "url": "https://data.europa.eu/data/datasets/covid-19-coronavirus-data-daily-up-to-14-december-2020",
        "license": "CC0: Public Domain",
        "license_url": "https://creativecommons.org/publicdomain/zero/1.0/",
    },
    "credit_card": {
        "description": "Anonymized credit card transactions labeled as fraudulent or genuine",
        "source": "Kaggle",
        "creators": "Machine Learning Group - ULB and Andrea",
        "url": "https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud",
        "license": "Database Contents License (DbCL) v1.0",
        "license_url": "http://opendatacommons.org/licenses/dbcl/1.0/",
    },
    "cpu": {
        "description": "Synthetic dataset of CPU pricing and performance characteristics.",
        "source": "DataDepot",
        "creators": "J. van Raak",
        "url": "https://github.com/vanraak/datadepot",
        "license": "CC BY 4.0",
        "license_url": "http://creativecommons.org/licenses/by/4.0/",
    },
    "credit": {
        "description": "700 good and 300 bad credits with 20 predictor variables. Data from 1973 to 1975.",
        "source": "UCI  Irvine Machine Learning Repository",
        "creators": "UCI Irvine and Hans Hofmann (original author)",
        "url": "https://doi.org/10.24432/C5QG88",
        "license": "CC BY 4.0",
        "license_url": "https://creativecommons.org/licenses/by/4.0/",
    },
    "diamonds": {
        "description": "Diamonds dataset",
        "source": "ggplot2",
        "creators": "ggplot2",
        "url": "https://ggplot2.tidyverse.org/reference/diamonds.html",
        "license": "MIT",
        "license_url": "https://ggplot2.tidyverse.org/LICENSE.html",
    },
    "drug": {
        "description": "Drug classification dataset.",
        "source": "LiveR - R Package",
        "creators": "Reza Mohammadi",
        "url": "https://cran.r-project.org/web/packages/liver/",
        "license": "GPL-3",
        "license_url": "https://cran.r-project.org/web/licenses/GPL-3",
    },
    "gapminder": {
        "description": "Gapminder dataset.",
        "source": "Gapminder.org",
        "creators": "Gapminder",
        "url": "https://www.gapminder.org/data/",
        "license": "CC BY 4.0",
        "license_url": "https://creativecommons.org/licenses/by/4.0/",
    },
    "hotel_city": {
        "description": "Hotel booking demand datasets: City Hotels",
        "source": "Antonio, de Almeida and Nunes (2019)",
        "creators": "Nuno Antonio, Ana de Almeida, and Luis Nunes",
        "url": "https://doi.org/10.1016/j.dib.2018.11.126",
        "license": "CC BY 4.0",
        "license_url": "http://creativecommons.org/licenses/by/4.0/",
    },
    "hotel_resort": {
        "description": "Hotel booking demand datasets: Resort Hotels",
        "source": "Antonio, de Almeida and Nunes (2019)",
        "creators": "Nuno Antonio, Ana de Almeida, and Luis Nunes",
        "url": "https://doi.org/10.1016/j.dib.2018.11.126",
        "license": "CC BY 4.0",
        "license_url": "http://creativecommons.org/licenses/by/4.0/",
    },
    "house": {
        "description": "Real Estate Valuation",
        "source": "UCI Irvine Machine Learning Repository",
        "creators": "I-Cheng Yeh",
        "url": "https://archive.ics.uci.edu/dataset/477/real+estate+valuation+data+set",
        "license": "CC BY 4.0",
        "license_url": "https://creativecommons.org/licenses/by/4.0/",
    },
    "house_price": {
        "description": "House price dataset.",
        "source": "Kaggle",
        "creators": "Kaggle",
        "url": "https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data",
        "license": "MIT",
        "license_url": "https://www.mit.edu/~amini/LICENSE.md",
    },
    "insurance": {
        "description": "Insurance dataset.",
        "source": "Kaggle",
        "creators": "Miri Choi",
        "url": "https://www.kaggle.com/datasets/mirichoi0218/insurance/data",
        "license": "Database Contents License (DbCL) v1.0",
        "license_url": "https://opendatacommons.org/licenses/dbcl/1-0/",
    },
    "las_vegas": {
        "description": "The dataset consists of quantitative and qualitative features derived from online reviews of 21 hotels on the Las Vegas Strip, collected from TripAdvisor.",
        "source": "UC Irivine Machine Learning Repository",
        "creators": "S. Moro, P. Rita and J. Coelho",
        "url": "https://doi.org/10.24432/C5QG7W",
        "license": "CC BY 4.0",
        "license_url": "http://creativecommons.org/licenses/by/4.0/",
    },
    "loan": {
        "description": "The loan approval dataset is a collection of financial records and associated information used to determine the eligibility of individuals or organizations for obtaining loans from a lending institution.",
        "source": "Kaggle",
        "creators": "KAI",
        "url": "https://www.kaggle.com/datasets/architsharma01/loan-approval-prediction-dataset",
        "license": "MIT",
        "license_url": "https://www.mit.edu/~amini/LICENSE.md",
    },
    "machine_failure": {
        "description": "Machine Failure Prediction using Sensor data",
        "source": "Kaggle",
        "creators": "Ume Naeem",
        "url": "https://www.kaggle.com/datasets/umerrtx/machine-failure-prediction-using-sensor-data",
        "license": "Apache 2.0",
        "license_url": "https://www.apache.org/licenses/LICENSE-2.0",
    },
    "mpg": {
        "description": "Auto MPG dataset.",
        "source": "UCI  Irvine Machine Learning Repository",
        "creators": "",
        "url": "https://archive.ics.uci.edu/ml/datasets/auto+mpg",
        "license": "CC BY 4.0",
        "license_url": "https://creativecommons.org/licenses/by/4.0/",
    },
    "red_wines": {
        "description": "Red wine quality dataset.",
        "source": "UCI  Irvine Machine Learning Repository",
        "creators": "",
        "url": "https://archive.ics.uci.edu/ml/datasets/wine+quality",
        "license": "CC BY 4.0",
        "license_url": "https://creativecommons.org/licenses/by/4.0/",
    },
    "vehicle": {
        "description": "Data on car prices, obtained from Car Dekho.",
        "source": "Kaggle",
        "creators": "Nehal Birla, Nishant Verma and Nikhil Kushwaha",
        "url": "https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho",
        "license": "Database Contents License (DbCL) v1.0",
        "license_url": "http://opendatacommons.org/licenses/dbcl/1.0/",
    },
    "white_wines": {
        "description": "White wine quality dataset.",
        "source": "UCI  Irvine Machine Learning Repository",
        "creators": "",
        "url": "https://archive.ics.uci.edu/ml/datasets/wine+quality",
        "license": "CC BY 4.0",
        "license_url": "https://creativecommons.org/licenses/by/4.0/",
    },
    "wholesale": {
        "description": "Wholesale customers dataset.",
        "source": "UCI  Irvine Machine Learning Repository",
        "creators": "Margarida Cardoso",
        "url": "https://archive.ics.uci.edu/dataset/292/wholesale+customers",
        "license": "CC BY 4.0",
        "license_url": "https://creativecommons.org/licenses/by/4.0/",
    },
}


def _normalize(name: str) -> str:
    """Normalize dataset names for flexible lookup."""
    return name.strip().lower().replace("_", "")


def _lookup_name(name: str) -> str:
    """Return canonical dataset name."""
    lookup = {k.replace("_", ""): k for k in DATASETS}
    key = _normalize(name)

    if key not in lookup:
        raise ValueError(f"Dataset '{name}' does not exist.")

    return lookup[key]


def load(name: str) -> pd.DataFrame:
    """Load a dataset as a pandas DataFrame."""
    canonical_name = _lookup_name(name)

    try:
        csv_file = importlib.resources.files("datadepot.data").joinpath(
            f"{canonical_name}.csv.gz"
        )
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
    print(f"{'Creators':<{width}}: {meta.get('creators','')}")
    print(f"{'URL':<{width}}: {meta.get('url','')}")
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
