# DynsDNS-updater

This package allows to update dynamic IP.

## Installation

### For users

Install the package [from GitHub](https://pip.pypa.io/en/stable/reference/pip_install/#git).

```bash
(venv) C:\Users\Adrien>pip install git+https://github.com/afaucon/DynDNS-updater.git@v0.0.1
(venv) C:\Users\Adrien>pip list
```

### For developpers

Clone the package from GitHub and install it in editable mode (i.e. [setuptools "develop mode"](https://setuptools.readthedocs.io/en/latest/setuptools.html#development-mode)).

```bash
(venv) C:\Users\Adrien>git clone git+https://github.com/afaucon/DynDNS-updater.git
(venv) C:\Users\Adrien>pip install --editable DynDNS-updater
(venv) C:\Users\Adrien>pip list
```

## Usage

Within a python module:

```python
import dyndns_updater

dyndns_updater.__author__
dyndns_updater.__version__
```

```python
from dyndns_updater import duckdns_update

ipv4, hasChanged = duckdns_update(yourdomain, yourtoken)
```

With the command line interface:

```bash
(venv) C:\Users\Adrien>python -m dyndns_updater --platform duckdns update yourdomain yourtoken
```

Or directly:

```bash
(venv) C:\Users\Adrien>dyndns_updater --platform duckdns update yourdomain yourtoken
```
