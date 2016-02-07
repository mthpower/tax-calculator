# Tax Calculator

A simple tax calculator. It's main interface is it's CLI, although it could be called from Python.


## Installation

You can install it from source by running from the root directory:
```
$ pip install -e .
```

Or the Makefile can be used to generate a debian package, currently targeting Ubuntu 14.04.
```
$ make dpkg
```

## Tests

The tests can be run via calling tox.


## Usage
Once installed, the package will have symlinked the `tax-calc` command to `/usr/local/bin`, which should be on your path.
```
$ tax-calc --help
Usage: tax-calc [OPTIONS] COUNTRY PRODUCT PRICE CURRENCY

Options:
  --verbose  verbose
  --help     Show this message and exit.
```
Example:
```
$ tax-calc GBR BREAD 2.50 GBP
0.50 GBP
```
