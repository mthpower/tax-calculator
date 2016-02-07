# -*- coding: utf-8 -*-
"""
Implementations of tax rules.

It is expected that tax rules conform to an interface, which is informally
specified here. Tax rules are expected to take a price, which should be a
Money object, and to return either a Money object, or a TaxResult object.

Partial functions are used here to "subclass" functions with pre-baked
parameters, to represent the specific tax laws of countries.

More generally there are only a handful of ways you can implement a tax law,
which are represented by the functions here. The intention of the interface
is such that more complicated tax laws could be implemented by chaining the
functions together.

For example, the UK income tax scheme could be implemented by chaining
`tax_band` functions with `percent` functions.

I saw the main requirements for tax functions as that they need to be
chainable and composable, and this was the simpliest way I could achieve
that without needing to write heavy class definitions and APIs for them.
"""
from collections import namedtuple
from decimal import Decimal
from functools import partial

from moneyed.classes import Money as M

TaxResult = namedtuple('TaxResult', ['tax', 'next_amount'])


def percent(price, percent):
    return Decimal(percent) % price

VAT = partial(percent, percent='20')
ZERO_PC = partial(percent, percent='0')
TEN_PC = partial(percent, percent='10')
TWENTY_FIVE_PC = partial(percent, percent='25')
THIRTY_PC = partial(percent, percent='30')


def flat(price, amount):
    return amount

GBR_WINE = partial(flat, amount=M('2', currency='GBP'))


def tax_band(price, amount, rule):
    curr = price.currency
    # If we're wholly in this tax band, don't pass a negative amount onwards.
    next_amount = max((price - amount), M('0', curr))

    # Only pay tax on this band, or the price, whichever is smaller.
    payable = min(price, amount)
    tax = rule(payable)
    return TaxResult(tax=tax, next_amount=next_amount)


DEDUCT_TWO_EUR = partial(tax_band, amount=M('2', 'EUR'), rule=ZERO_PC)
