# Capstone Proposal - Allstate: How severe is an insurance claim?
![Python 3](https://img.shields.io/badge/Python-3-blue.svg)
![License](https://img.shields.io/badge/Code%20License-MIT-blue.svg)

## Describe project
 This project is my Capstone in course Udacity Machine Learning Engineer Nanodegree.

## Objective
The objective is use supervised learning technical for understend how severe is an insurance claim.

## Documentation
- [Capstone proposal](reports/)
- [Report this project](reports/)

## Datasource
The datasource is: https://www.kaggle.com/c/allstate-claims-severity/data

## Algoritms
- Linear Regression
- Random Forest Regressor
- XGBoost

## Quickstart
1. [Data Exploration and Data Cleaning](notebooks/)
2. [Modeling and Evaluation](notebooks/)

## Struture this Project
```
.
├── data
│   ├── cleansing
│   │   ├── test.csv
│   │   └── train.csv
│   ├── raw
│   │   ├── sample_submission.csv
│   │   ├── test.csv
│   │   └── train.csv
│   └── submissions-kaggle
│       ├── lin_regression_submission.csv
│       ├── random_forest_submission.csv
│       └── xgb_submission.csv
├── LICENSE
├── notebooks
│   ├── 1-data-exploration-and-data-cleaning.ipynb
│   └── 2-algoritm-selection-and-tranning-model.ipynb
├── README.md
├── references
│   └── images
│       └── allstate.jpg
├── reports
│   ├── capstone-proposal.md
│   ├── images
│   │   ├── corr_cont_types_13_ate_14.png
│   │   ├── corr_cont_types_1_ate_4.png
│   │   ├── corr_cont_types_5_ate_8.png
│   │   ├── corr_cont_types_all.png
│   │   ├── corr_matrix_cont.png
│   │   ├── default_loss.png
│   │   ├── describe-cat.png
│   │   ├── describe-continuos2.png
│   │   ├── describe-continuos.png
│   │   ├── distribuicao.png
│   │   ├── linear_regression-1.png
│   │   ├── linear_regression-2.png
│   │   ├── log_loss.png
│   │   ├── mae.png
│   │   ├── PCA.png
│   │   ├── random_forest-1.png
│   │   ├── random_forest-2.png
│   │   ├── random_forest-3.png
│   │   ├── test_data.png
│   │   ├── train_data.png
│   │   ├── xgboost-1.png
│   │   ├── xgboost-2.png
│   │   └── xgboost-3.png
│   ├── machine-learning-capstone.md.ipynb
│   ├── proposta.pdf
│   └── relatorio_machine-learning-capstone.pdf
└── src
    ├── environment
    │   ├── config_environment.txt
    │   ├── container
    │   │   └── Dockerfile
    │   ├── create_requirements.sh
    │   ├── create_virtual_env.sh
    │   ├── __init__.py
    │   ├── jupyter_notebook_config.py
    │   ├── makefile
    │   ├── prepare_env.py
    │   ├── README.md
    │   ├── requirements.txt
    │   ├── show_config_environment.sh
    │   ├── show_struture_project.sh
    │   ├── struture_project.txt
    │   ├── test_environment.py
    │   ├── venv
    │   └── virtualenv_requirements.txt
    ├── __init__.py
    └── visualization
        ├── hidden_code.js
        └── visuals.py

14 directories, 58 files
```

## Requirements
This project is tested with:

| Requisite      | Version  |
|----------------|----------|
| Python         | 3.6.8    |
| Pip            | 21.2.4   |
| Git            | 2.25.1   |

I recommend using Python [venv](https://github.com/brunocampos01/becoming-a-expert-python#virtual-environment).

## Running
1. Clone this repository
```sh
git clone https://github.com/brunocampos01/challenge-keyrus
cd challenge-keyrus
```

2. Choose which environment to running
 - [local](src/environment/README.md)
 - [virtual environment](src/environment/README.md)
 - [container](src/environment/README.md)

3. In terminal running command `jupyter-notebook` and navigate in this repository: `notebooks`

##### NOTES
- All the development was done using **virtualenv**. 
- To learn more about the environment that has been developed, access the file [config_environment.txt](src/environment/config_environment.txt)

---

<p  align="left">
<br/>
<a href="mailto:brunocampos01@gmail.com" target="_blank"><img src="https://github.com/brunocampos01/devops/blob/master/images/email.png" alt="Gmail" width="30">
</a>
<a href="https://stackoverflow.com/users/8329698/bruno-campos" target="_blank"><img src="https://github.com/brunocampos01/devops/blob/master/images/stackoverflow.png" alt="GitHub" width="30">
</a>
<a href="https://www.linkedin.com/in/brunocampos01" target="_blank"><img src="https://github.com/brunocampos01/devops/blob/master/images/linkedin.png" alt="LinkedIn" width="30"></a>
<a href="https://github.com/brunocampos01" target="_blank"><img src="https://github.com/brunocampos01/devops/blob/master/images/github.png" alt="GitHub" width="30"></a>
<a href="https://brunocampos01.netlify.app/" target="_blank"><img src="https://github.com/brunocampos01/devops/blob/master/images/blog.png" alt="Website" width="30">
</a>
<a href="https://medium.com/@brunocampos01" target="_blank"><img src="https://github.com/brunocampos01/devops/blob/master/images/medium.png" alt="GitHub" width="30">
</a>
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png",  align="right" /></a><br/>
</p>

