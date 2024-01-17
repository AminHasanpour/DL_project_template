import os
import shutil
from keyword import iskeyword

project_name = '{{cookiecutter.project_name}}'
use_wandb = True if '{{cookiecutter.use_wandb}}'.lower() == 'y' else False
use_docker = True if '{{cookiecutter.use_docker}}'.lower() == 'y' else False

if not project_name.isidentifier() or not project_name.islower():
    raise ValueError(
        "\n"
        "Project name must be a valid project name, meaning that it must be a valid Python name and also be lowercase." 
        " This means that it must not contain spaces or special characters, and must not start with a number."
        " In general it is best to use only lowercase letters and underscores."
        " You can read more about Python naming conventions for packages here:"
        " https://peps.python.org/pep-0008/#package-and-module-names"
        "\n"
    )
if iskeyword(project_name):
    raise ValueError('Project name must not be a build-in keyword, as it will cause syntax errors.')

if not use_docker:
    try:
        shutil.rmtree(os.path.join(project_name, "docker_files"))
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))