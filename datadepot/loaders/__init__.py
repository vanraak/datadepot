from .csv_loader import load as csv_loader
from .openml_loader import load as openml_loader
from .seaborn_loader import load as seaborn_loader
from .tensorflow_loader import load as tensorflow_loader

LOADERS = {
    "csv": csv_loader,
    "openml": openml_loader,
    "seaborn": seaborn_loader,
    "tensorflow": tensorflow_loader,
}


def get_loader(name: str):
    return LOADERS[name]
