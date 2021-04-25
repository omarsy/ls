# LS [![GitHub Actions status | omarsy/ls](https://github.com/omarsy/ls/workflows/Push/badge.svg)](https://github.com/omarsy/ls/actions?workflow=Push)


# Requirements

Python 3.6+.



# Dependencies

Dependencies are defined in:

- ``requirements_win.txt``: For windows OS

- ``requirements.txt``: Others OS

# Testing


## Unit Testing

```sh
python -m unittest
```

## Scenario

```sh
python -m behave ./test/features --tags=linux,windows
```

# Run

```
usage: ls.py [-h] [-l] path

lists files of a specified folder.

positional arguments:
  path        path of the folder if the folder exist or path + prefix

optional arguments:
  -h, --help  show this help message and exit
  -l          display the mode and the creation date of the files
```

## Example

```sh
python ls.py  ./l -l
```