# -*- coding: utf-8 -*-
from decimal import Decimal
from functools import partial, wraps


def decimalise(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, str):
                raise ValueError

        for kwd, value in kwargs.items():
            if not isinstance(kwd, str):
                raise ValueError

        args = [Decimal(arg) for arg in args]
        kwargs = {k: Decimal(v) for k, v in kwargs.items()}

        return func(*args, **kwargs)
    return wrapper


@decimalise
def percent(price, percent):
    as_coeff = percent / 100
    return price * as_coeff

VAT = partial(percent, percent='20')
UK_CIG = partial(percent, percent='25')
GER_CIG = partial(percent, percent='30')
DEFAULT = partial(percent, percent='10')


@decimalise
def flat(price, amount):
    return amount

UK_WINE = partial(flat, amount='2')
