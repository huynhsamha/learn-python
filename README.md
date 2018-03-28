# learn-python
Getting started with python

## Visual Studio Code
[Document here](https://code.visualstudio.com/docs/python/python-tutorial)

Some configuration (my OS is **Ubuntu 16.04**):

### Install `pip`
```
sudo apt-get install python-pip
```

### Linter with `pylint`

Install `pylint`

```
pip install pylint
```

Config vscode settings

In `settings.json` add
```json
{
    "python.linting.pylintPath": "~/.local/bin/pylint"
}
```

### Format with 'autopep8'

Install `autopep8`

```
pip install pep8
pip install --upgrade autopep8
```

Config vscode settings

In `settings.json` add
```json
{
    "python.formatting.autopep8Path": "~/.local/bin/autopep8"
}
```

### Install `pip3` for `python3`
```
sudo apt-get update
sudo apt-get -y install python3-pip
pip3 --version
```

### Install and Usage with `virtualenv`
`virtualenv` is virtual environment for python interpreter. It's useful for privacy project python, not use as global on your system.

#### Installation

```
pip install virtualenv
```

#### Usage
1. Create Virtual Environment
In `~/`, create new virtual environment python by:
```
virtualenv python-virtualenv
```
or use following line to use with python3
```
virtualenv -p python3 python-virtualenv
```
It will create new folder `python-virtualenv` (you can use other name).

2. Activate and Deactivate virtualenv
In terminal:
```
source ~/python-virtualenv/bin/activate
```
It will config python run from here
To deactivate, run:
```
deactivate
```

3. VS Code settings
Change `pythonPath` and `linting/pylintPath` with path virtualenv.

```json
{
    "python.pythonPath": "~/python-virtualenv/bin/python3.5",
    "python.linting.pylintPath": "~/python-virtualenv/bin/pylint",
}
```