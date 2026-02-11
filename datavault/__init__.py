from ._version import __version__
from .datasets import load, datasets, dataset_table


def version():
    """Prints DataVault package version."""
    print(f"Version: {__version__}")


__all__ = ["load", "datasets", "dataset_table"]

__doc__ = f"""
DataVault package: Example datasets for Python users

Available datasets:
{dataset_table()}

# Load a dataset from the DataVault package as a pandas DataFrame

>>> import datavault
>>> df = datavault.load('<dataset_name>')  # Load a dataset as a pandas DataFrame

# Show the version of the DataVault library:
>>> datavault.version()  # DataVault version {__version__}
"""
