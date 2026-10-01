# `datadepot`

![](https://raw.githubusercontent.com/vanraak/datadepot/main/logo_small.png)

This library  provides a simple interface for loading datasets used in the book *Data Science Foundations and Machine Learning with Python*.

## Installation

Install datadepot with pip:

```bash
pip install datadepot
```

or with conda:

```bash
conda install conda-forge::datadepot
```

## Usage

Import datadepot and load a dataset:

```python
import datadepot

df = datadepot.load("<dataset>")
```

Replace `<dataset>` with the name of the dataset you want to load. For example:

```python
df = datadepot.load("bank_marketing")
```

The return format depends on the dataset. Some datasets return a single DataFrame, while others return train/test splits or other structured data.

## Dataset Information

View metadata for any dataset:

```python
datadepot.info("<dataset>")
```

Example:

```python
datadepot.info("diamonds")
```

This displays the dataset metadata:

- Description
- Source
- URL
- Creators
- License
- License URL

## Available Datasets

The following datasets can be loaded:

- adult
- auto_mpg
- bank_marketing
- bike_sharing
- churn
- cpu
- credit_card_fraud
- credit_default
- diamonds
- fashion_mnist
- hotel_booking
- imdb
- laptop
- loan_approval
- mnist
- nyc_taxi
- online_shoppers
- real_estate
- wine_quality

More information about each dataset is available at <https://datasciencebook.ai/datadepot>, including its description, source, creators, and license.

## License

datadepot is distributed under the MIT License. Individual datasets may be subject to different licenses; see each dataset's metadata for details.