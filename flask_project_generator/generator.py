import os

def create_flask_project(project_name):
    # Dossiers à créer
    directories = [
        project_name,
        os.path.join(project_name, 'app'),
        os.path.join(project_name, 'app/static'),
        os.path.join(project_name, 'app/templates'),
    ]

    # Fichiers à créer avec leur contenu
    files_content = {
        os.path.join(project_name, 'run.py'): """from app import app

if __name__ == "__main__":
    app.run(debug=True)
""",
        os.path.join(project_name, 'app/__init__.py'): """from flask import Flask

app = Flask(__name__)

from app import routes
""",
        os.path.join(project_name, 'app/routes.py'): """from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
"""
    }

    # Création des dossiers
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        # print(f"Dossier créé: {directory}")

    # Création des fichiers avec leur contenu
    for filepath, content in files_content.items():
        with open(filepath, 'w') as file:
            file.write(content)
        # print(f"Fichier créé: {filepath}")

    print("Projet Flask généré avec succès.")
    
def main():
    project_name = input("Entrez le nom du projet Flask: ")
    create_flask_project(project_name)
