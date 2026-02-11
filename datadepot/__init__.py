from ._version import __version__
from .datasets import load, datasets, dataset_table


def version():
    """Prints DataDepot package version."""
    print(f"Version: {__version__}")


__all__ = ["load", "datasets", "dataset_table"]

__doc__ = f"""
DataDepot package: Example datasets for Python users

Available datasets:
{dataset_table()}

# Load a dataset from the DataDepot package as a pandas DataFrame

>>> import datadepot
>>> df = datadepot.load('<dataset_name>')  # Load a dataset as a pandas DataFrame

# Show the version of the DataDepot library:
>>> datadepot.version()  # DataDepot version {__version__}
"""
