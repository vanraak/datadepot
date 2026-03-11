# __init__.py
from ._version import __version__
from .datasets import load, dataset_table, info


def version():
    """Prints DataDepot package version."""
    print(f"Version: {__version__}")


__all__ = ["load", "dataset_table", "info", "version"]

# Dynamic package docstring with available datasets
__doc__ = f"""
DataDepot package: Example datasets for Python users

Available datasets:
{dataset_table()}

# Load a dataset from the DataDepot package as a pandas DataFrame
>>> import datadepot
>>> df = datadepot.load('<dataset_name>')  # Load dataset

# Show dataset info and metadata:
>>> datadepot.info('<dataset_name>')       # Pretty-print dataset metadata
>>> meta = datadepot.info('<dataset_name>', return_dict=True)  # Get dict

# Show the version of the DataDepot library:
>>> datadepot.version()  # DataDepot version {__version__}
"""
