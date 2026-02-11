# Package `datadepot`


**Package ‘datadepot’**

**Title** \`\`DataDepot’’

**Description**

The **datadepot** package provides a collection of datasets used in the book `Data Science Foundations and Machine Learning with Python`.

**URL** <https://github.com/vanraak/datadepot>

**Depends** Python (\>= 3.8) and Pandas (\>2.0)

**License** GPL (\>= 2)

**Repository** Pypi

**Authors** Jeroen van Raak and Reza Mohammadi

**Maintainer** Jeroen van Raak, <j.j.f.vanraak@uva.nl>

**NeedsCompilation** no

**Installation**

    pip install datadepot

**Usage**

    import datadepot
    df=datadepot.load('<dataset>')

Replace <dataset> with the name of the dataset, such as ‘bank’, ‘house’, or ‘churn’.

**Example**

    df=datadepot.load('bank') # Load the bank dataset.

**Datasets**

The following datasets are included:

- adult
- advertising
- bank
- caravan
- cereal
- churn
- churn_ibm
- churn_tel
- corona
- diamonds
- drug
- gapminder
- house
- house_price
- insurance
- marketing
- mpg
- red_wines
- risk
- white_wines

**Documentation**

The full documentation is available at:
<https://github.com/vanraak/datadepot/blob/main/README.pdf>
