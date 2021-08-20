# PYTHON DISK USAGE

Takes a path as an argument and returns it's total disk usage recursively.

## INSTALLATION

`pip install pdu`

## CLI USAGE

```
usage: pdu [-h] [path]

Python Disk Usage Calculator.

positional arguments:
  path        A valid path.

optional arguments:
  -h, --help  show this help message and exit
```

## PYTHON USAGE

```python
path = '/path/to/some/file/or/directory'

from pdu import du

human_readable_size = du(path)

from pdu import calc

size_in_bytes = calc(path)

from pdu import convert

human_readable_units = convert(bytes)
```
