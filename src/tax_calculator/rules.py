# -*- coding: utf-8 -*-
from collections import namedtuple
from decimal import Decimal
from functools import partial

from moneyed.classes import Money as M

TaxResult = namedtuple('TaxResult', ['tax', 'next_amount'])


def percent(price, percent):
    return Decimal(percent) % price

VAT = partial(percent, percent='20')
TEN_PC = partial(percent, percent='10')
TWENTY_FIVE_PC = partial(percent, percent='25')
THIRTY_PC = partial(percent, percent='30')


def flat(price, amount):
    return amount

UK_WINE = partial(flat, amount=M('2', currency='GBP'))


def tax_band(price, amount):
    curr = price.currency
    next_amount = price + amount
    return TaxResult(tax=M('0', curr), next_amount=next_amount)


DEDUCT_TWO_EUR = partial(tax_band, amount=M('-2', 'EUR'))
