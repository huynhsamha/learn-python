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