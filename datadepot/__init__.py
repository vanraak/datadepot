from ._version import __version__
from .core import load, dataset_table, list_datasets, info, load_zones


def version():
    """Return DataDepot package version."""
    return __version__


__all__ = [
    "load",
    "dataset_table",
    "info",
    "version",
    "load_zones",
]


__doc__ = f"""
DataDepot package: Example datasets for Python users

Available datasets:
{dataset_table()}

# Load a dataset as a pandas DataFrame
>>> import datadepot
>>> df = datadepot.load('<dataset_name>')

# Show dataset info and metadata:
>>> datadepot.info('<dataset_name>')
>>> meta = datadepot.info('<dataset_name>', return_dict=True)

# Show the version of the DataDepot library:
>>> datadepot.version()
'{__version__}'
"""
