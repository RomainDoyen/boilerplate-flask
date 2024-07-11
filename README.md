# Un script pour générer des projets Flask.

Un package Python installable pour générer des projets Flask.

## La structure de dossiers du package

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

## Fichiers du package

- **`generator.py`** : Contient la logique de création du projet.

- **`__init__.py`** : Pour marquer le répertoire comme un package Python.

- **`setup.py`** : Fichier de configuration pour `setuptools`.

- **`README.md`** : Description du package.

- **`MANIFEST.in`** : Inclut des fichiers supplémentaires dans le package si nécessaire.

## Installation

Instructions pour la mise en place :

- Naviguez jusqu'au dossier racine (flask_project_generator/).
- Installez le package avec la commande : 

```bash
pip install .
```

## Utilisation

Pour générer un projet Flask, exécutez la commande suivante :

```bash
generate-flask-project
```