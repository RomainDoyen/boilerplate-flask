# A script to generate Flask projects.

An installable Python package for generating Flask projects.

## Package folder structure

```bash
│   LICENSE
│   MANIFEST.in
│   README.md
│   setup.cfg
│   setup.py
│
└───flask_project_generator
        generator.py
        __init__.py
```

## Package files

- **`generator.py`** : Contains project creation logic.

- **`__init__.py`** : To mark the directory as a Python package.

- **`setup.py`** : Configuration file for `setuptools`.

- **`README.md`** : Package description.

- **`MANIFEST.in`** : Includes additional files in the package if required.

## Installation

Set-up instructions :

- Navigate to the root folder (flask_project_generator/).
- Install the package with the command : 

```bash
pip install .
```

## Use

To generate a Flask project, run the following command:

```bash
generate-flask-project
```