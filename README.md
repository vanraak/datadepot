# Package `datadepot`


**Package ‘datadepot’**

**Title** DataDepot

![](https://raw.githubusercontent.com/vanraak/datadepot/main/logo_small.png)


**Description**

The **datadepot** package provides a collection of datasets used in the book `Data Science Foundations and Machine Learning with Python`.

**URL** <https://github.com/vanraak/datadepot>

**Depends** Python (\>= 3.10) and Pandas (\>2.0)

**License** GPL (\>= 2)

**Repository** Pypi

**Authors** Jeroen van Raak

**Maintainer** Jeroen van Raak, <j.j.f.vanraak@uva.nl>

**NeedsCompilation** no

**Installation**

    pip install datadepot

    or:

    conda install conda-forge::datadepot

**Usage**

    import datadepot
    df=datadepot.load("<dataset>")

Replace <dataset> with the name of the dataset, such as "bank", "house", or "churn".

**Example**

    df=datadepot.load('bank') # Load the bank dataset.

**Datasets**

The following datasets are included:

- adult
- bank
- cereal
- churn
- churn_ibm
- churn_mlc
- covid
- credit
- credit_card
- cpu
- diamonds
- drug
- gapminder
- hotel_city
- hotel_resort
- house
- house_price
- insurance
- las_vegas
- loan
- machine_failure
- mpg
- red_wines
- vehicle
- white_wines
- wholesale

**Documentation**

The full documentation is available at:
<https://github.com/vanraak/datadepot/blob/main/README.pdf>
