 # Capstone Proposal - Allstate Claims Severity
 [![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
 ![License](https://img.shields.io/badge/Code%20License-MIT-blue.svg)

  ## Describe project
 This project is my Capstone in course Udacity Machine Learning Engineer Nanodegree.<br/>

 - The objective is use supervised learning technical for understend how severe is an insurance claim.
 - The datasource is: https://www.kaggle.com/c/allstate-claims-severity/data
 - Learn more proposal in: https://github.com/brunocampos01/allstate-claims-severity/tree/master/reports


 ## Quickstart
- [Data Cleanning and Feature Engineering](notebooks/allstate_corporation-casptone_nanodegreed.ipynb)

- [Modeling](notebooks/allstate_corporation-casptone_nanodegreed.ipynb)

## Algoritms
- Linear Regression
- Random Forest Regressor
- XGBoost


## Requirements
- Python 3.7.3 or more:<br/>
```sh
sudo apt-get install Python3.7.3
```

- pip
```
sudo apt-get install python3-pip
```

- Libraries<br/>
Will be installed in real pip
```sh
pip3 install --user virtualenv==16.6.0
```

- Git
```sh
sudo apt-get install git
```

## Install
- Clone this repository
```sh
git clone https://github.com/brunocampos01/challenge-keyrus
```

- All the development was done using **virtualenv**. To perform under the same conditions follow the steps below:
  - Create a virtualenv
  ```sh
  virtualenv -p python3 venv_keyrus
  ```

  - Activate this semi-isolated environment
  ```sh
  source venv_keyrus/bin/activate
  ```

  - Install the libraries
  ```sh
  pip3 install -r src/environment/config_environment.txt   # libs necessary to prepare virtual environment
  pip3 install -r src/environment/environment.txt          # libs necessary in notebooks
  ```

 ---

## Author
- Bruno Aurélio Rôzza de Moura Campos (brunocampos01@gmail.com)

## Copyright
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Bruno A. R. M. Campos</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
