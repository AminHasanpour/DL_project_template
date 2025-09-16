# 🍪 A up-to-date Cookiecutter template for MLOps

---

Taken from [MLOps template](https://github.com/SkafteNicki/mlops_template). This template has been updated 
to better fit deep learning projects and contain more features out of the box.

## Requirements to use the template:

* Python 3.12
* Cookiecutter v2.4.0

## Start a new project

On your local machine run

```bash
cookiecutter https://github.com/AminHasanpour/mlops_template
```

and input starting values for the project. Note that when asked for the project name, you should input
a [valid Python package name](https://peps.python.org/pep-0008/#package-and-module-names). This means that the name 
should be all lowercase and only contain letters, numbers and underscores. The project name will be used as the name of 
the Python package. This will automatically be validated by the template.

## The stack

🐍 Python projects using `pyproject.toml` <img src="icons/python.svg" width="20" height="20">

🔥 Models in `pytorch` <img src="icons/pytorch.svg" width="20" height="20">

📦 Containerized using `docker` <img src="icons/docker.svg" width="20" height="20">

📄 Documentation in `mkdocs` <img src="icons/markdown.svg" width="20" height="20">

👕 Linting and formatting with `ruff` <img src="icons/ruff.svg" width="20" height="20">

✅ Checking using `pre-commit` <img src="icons/precommit.svg" width="20" height="20">

🛠️ CI with `Github actions` <img src="icons/githubactions.svg" width="20" height="20">

and more...