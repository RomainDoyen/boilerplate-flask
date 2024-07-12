import os
from colorama import Fore, Style, init

def create_flask_project(project_name):
    # Folders to create
    directories = [
        project_name,
        os.path.join(project_name, 'app'),
        os.path.join(project_name, 'app/static'),
        os.path.join(project_name, 'app/templates'),
    ]

    # Files to create with their contents
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

    # Creating folders
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        # print(f"File created: {directory}")

    # Creating files with their contents
    for filepath, content in files_content.items():
        with open(filepath, 'w') as file:
            file.write(content)
        # print(f"File created: {filepath}")

    print(f"\n{Fore.GREEN}Flask project successfully generated.{Style.RESET_ALL}\n")
    print(f"Install dependencies with: {Fore.BLUE}pip install Flask{Style.RESET_ALL}\n")
    print(f"Go to the project folder: {Fore.BLUE}cd {project_name}{Style.RESET_ALL}\n")
    print(f"Run the project with: {Fore.BLUE}python run.py{Style.RESET_ALL}\n")
    
def main():
    project_name = input("Enter the Flask project name: ")
    create_flask_project(project_name)
