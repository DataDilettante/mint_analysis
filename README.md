## Mint Analysis 
Financial analysis done through the use of Jupyter notebooks. This relies on
a CSV output from Mint.com of your financhial transactions. It is focuesd
primarily on spending and salaried income and has no support for investments
at this time. 

## Motivation
Mint is a great tool for tracking finances however there are several things 
missing from being able to effectively use it. For example, the inability
to add tags from a mobile device and the non-existant ability to view 
information based on tags. 

The libraries built here are an attempt to learn more about the abilities of
Pandas while also creating a useful analysis output to plan and adjust
budgets.

## To Do
- On import, mark the date column as a Date
- Combine the import and cleaning into one function with flags
- Create a function to auto detect all Lables and return them based on type


## Setup

### Data Sources
1. Go to Mint.com and download a `transactions.csv` file and put it into a 
data folder at the root of this repo. 
2. Open the Jupyter notebook that pertains to the information you're
interested in. Note these notebooks were built with the standard docker
containers created by Kaggle and can be pulled with `docker pull
kaggle/jupyter`

### Tags
This library makes some assumptions about how you organize your information in 
Mint's tracking. In order to make full use of the tag feature, it assumes
that your tags are only one work (no spaces) and that they are organized
by type using specific icons as indicators. 

* `@` - Used to denote a person or entitiy (ie. `@John`)
* `#` - Used to denote an activity or area of interest (ie. `#Running`)

## Code

### Libraries


### iPython Notebook
- analysis - Determine how much you spend and on what


