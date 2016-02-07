# -*- coding: utf-8 -*-
from decimal import Decimal

import pytest

from tax_calculator import calc


@pytest.mark.parametrize('inputs,tax', [
    (
        {
            'country': 'GBR',
            'product_code': 'BREAD',
            'price': '2.50'
        },
        Decimal('0.50')
    ),
    (
        {
            'country': 'GBR',
            'product_code': 'WINE75CL',
            'price': '5.00'
        },
        Decimal('2.00')
    ),
    (
        {
            'country': 'GBR',
            'product_code': 'CIG',
            'price': '8.00'
        },
        Decimal('2.00')
    ),
    # GER: Tax on cigarettes is 30% -> €2.40
    # GER: The first €2 on all products is not taxable -> €0.40
    (
        {
            'country': 'GER',
            'product_code': 'CIG',
            'price': '8.00'
        },
        Decimal('0.40')
    ),
    # GER: The first €2 on all products is not taxable
    # Unknown products taxed at 10%
    (
        {
            'country': 'GER',
            'product_code': 'FAIL',
            'price': '8.00'
        },
        Decimal('0.40')
    ),
    # Unknown Countries should be taxed at 10%
    (
        {
            'country': 'FAIL',
            'product_code': 'CIG',
            'price': '8.00'
        },
        Decimal('0.8')
    ),
])
def test_calculate_tax(inputs, tax):
    assert calc.calculate_tax(**inputs) == tax
