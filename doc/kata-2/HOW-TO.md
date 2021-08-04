
## Story 1: Explicitly declare and isolate dependencies

> Using principal from [12-factor](https://12factor.net/) app methodology.
 
### Objectives:
- Explicitly declare and isolate dependencies. (python virtual environments)
- Never rely on implicit existence of system-wide packages.
- Declare dependencies via a declaration manifest
- Dependency specification is applied uniformly to both production and development.

### Steps:
- Uninstall `requests` module using below command.
```shell
pip uninstall requests
```
- Execute `python notification.py`
- You should be getting below `ERROR`.
```
Traceback (most recent call last):
  File "notification.py", line 3, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'
```
#### Installing Pipenv
Pipenv is a dependency manager for Python projects.
##### macOS 
```shell
brew install pipenv
```
>Homebrew will keep `pipenv` and all of its dependencies in an isolated virtual environment so it doesn’t 
> interfere with the rest of your Python installation

##### Generic (windows, macOS etc)
```shell
pip install --user pipenv # restricting package installation to current user
```
> :point_right:  Follow this [link](https://pipenv-fork.readthedocs.io/en/latest/install.html#pragmatic-installation-of-pipenv) in case pipenv isn’t available in your shell after installation.
- Change directory to root and execute:
```shell
pipenv install requests --python 3.8.10 # or the python version you have
```
- You should get output similar to this (although the exact paths shown will vary):
```shell
Creating a Pipfile for this project...
Creating a virtualenv for this project...
Using base prefix '/usr/local/Cellar/python3/3.8.10/Frameworks/Python.framework/Versions/3.8'
New python executable in ~/.local/share/virtualenvs/tmp-agwWamBd/bin/python3.8
Also creating executable in ~/.local/share/virtualenvs/tmp-agwWamBd/bin/python
Installing setuptools, pip, wheel...done.
..
..
....
..
Adding requests to Pipfile's [packages]...
✔ Installation Succeeded
```
- This will create two files `Pipfile` and `Pipfile.lock` at the root of your project.
- Check the `requests` module version in `Pipfile.lock` or execute `pipenv run pip show requests` 
  on the command line.
```json
"requests": {
    "hashes": [
        "sha256:6c1246513ecd5ecd4528a0906f910e8f0f9c6b8ec72030dc9fd154dc1a6efd24",
        "sha256:b8aa58f8cf793ffd8782d3d8cb19e66ef36f7aba4353eec859e74678b01b07a7"
    ],
    "index": "pypi",
    "version": "==2.26.0"
```
- Replace `requests = "*"` to `requests = "==2.26.0"` in `Pipfile`. 
>This is to ensure everyone working on the project get the same version tested by you.
- Run the `notification.py`
```shell
pipenv run python aws_console_changes/notification.py
```
- You should have a notification in slack now.
- Commit the code to version control including BOTH `Pipfile` and `Pipfile.lock`
- onwards to [kata-3](../kata-3/HOW-TO.md)

#### Achieved objective? :thinking:
- Explicitly declare and isolate dependencies. :white_check_mark:
- Never rely on implicit existence of system-wide packages.  :white_check_mark:
  - No longer dependent on system wide packages to be available.
  - Simplifying setup.
  - The new developer can check out the app’s codebase onto their development machine, requiring only the language
    runtime (python3) and dependency manager (pipenv) installed as prerequisites.
  - Will be able to set up everything needed to run the app’s code with a deterministic build command (`pipenv install and run`).
- Declare dependencies via a declaration manifest. :white_check_mark:
  - Pipfile
- Dependency specification is applied uniformly to both production and development.  :white_check_mark:
