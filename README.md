# Capstone Proposal - Allstate Claims Severity
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
![License](https://img.shields.io/badge/Code%20License-MIT-blue.svg)

## Describe project
 This project is my Capstone in course Udacity Machine Learning Engineer Nanodegree.

 - The objective is use supervised learning technical for understend how severe is an insurance claim.
 - The datasource is: https://www.kaggle.com/c/allstate-claims-severity/data
 - Learn more proposal in: https://github.com/brunocampos01/allstate-claims-severity/tree/master/reports

## Quickstart
1. [Data Cleaning](https://github.com/brunocampos01/allstate-claims-severity/blob/master/notebooks/allstate_corporation-casptone_nanodegreed.ipynb
)
2. [Data Exploration](https://github.com/brunocampos01/allstate-claims-severity/blob/master/notebooks/allstate_corporation-casptone_nanodegreed.ipynb
)
3. [Feature Engineering](https://github.com/brunocampos01/allstate-claims-severity/blob/master/notebooks/allstate_corporation-casptone_nanodegreed.ipynb
)
4. [Model Selection](https://github.com/brunocampos01/allstate-claims-severity/blob/master/notebooks/allstate_corporation-casptone_nanodegreed.ipynb
)

## Struture this Project
```
.
├── corr_cont_types_13_ate_14.png
├── data
│   ├── raw
│   │   ├── sample_submission.csv
│   │   ├── test.csv
│   │   └── train.csv
│   └── submissions-kaggle
├── LICENSE
├── notebooks
│   └── allstate_corporation-casptone_nanodegreed.ipynb
├── README.md
├── references
│   └── images
│       └── allstate.jpg
├── reports
│   ├── capstone-proposal.md
│   ├── images
│   │   ├── corr_cont_types_13_ate_14.png
│   │   ├── corr_cont_types_1_ate_4.png
│   │   ├── default_loss.png
│   │   ├── describe-cat.png
│   │   ├── describe-continuos2.png
│   │   ├── describe-continuos.png
│   │   ├── distribuicao.png
│   │   ├── linear_regression-1.png
│   │   ├── linear_regression-2.png
│   │   ├── log_loss.png
│   │   ├── mae.png
│   │   ├── PCA.png
│   │   ├── random_forest-1.png
│   │   ├── random_forest-2.png
│   │   ├── random_forest-3.png
│   │   ├── test_data.png
│   │   ├── train_data.png
│   │   ├── xgboost-1.png
│   │   ├── xgboost-2.png
│   │   └── xgboost-3.png
│   ├── machine-learning-capstone.md.ipynb
│   ├── proposta.pdf
│   └── relatorio_machine-learning-capstone.pdf
├── requirements.txt
└── src
    ├── environment
    │   ├── config_environment.txt
    │   ├── create_requirements.sh
    │   ├── create_virtual_env.sh
    │   ├── __init__.py
    │   ├── makefile
    │   ├── prepare_env.py
    │   ├── README.md
    │   ├── show_config_environment.sh
    │   ├── show_struture_project.sh
    │   ├── struture_project.txt
    │   ├── test_environment.py
    │   └── virtualenv_requirements.txt
    ├── __init__.py
    └── notebook_config.ini

10 directories, 47 files
```

## Algoritms
- Linear Regression
- Random Forest Regressor
- XGBoost

## Requirements

- Python 3.7.1 or more
```sh
sudo apt install python3.7
```

- pip
```sh
sudo apt install python-pip
```

- Libraries<br/>
```sh
pip3 install -r requirements.txt            # libs necessary in notebooks
```


## Running
- [Running in Virtual Env Python (semi-isolated Environment)](#running-in-virtual-env-python)
- [Running in Container (isolated envinment)](#running-in-container)

#### Running in Virtual Env Python

##### If machine not contains Python and yours dependencies
1. Install Python Dependencies, Delete all compiled Python files, Test python environment

```shell script
sudo make

# Available rules:

# clean               Delete all compiled Python files
# lint                Lint using flake8
# requirements        Install Python Dependencies
# test_environment    Test python environment is setup correctly
```

```shell script
make requirements
make test_environment
make clean
```

2. Create virtual environment

```shell script
bash src/environment/create_virtual_env.sh
```

3. Activate this semi-isolated environment

```shell script
source src/environment/venv/bin/activate
```

4. Install the libraries

```shell script
pip3 install -r virtualenv_requirements.txt # libs necessary to prepare virtual environment
pip3 install -r requirements.txt            # libs necessary in notebooks
```

---

## Author
- Bruno Aurélio Rôzza de Moura Campos (brunocampos01@gmail.com)

## Copyright
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Bruno A. R. M. Campos</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
