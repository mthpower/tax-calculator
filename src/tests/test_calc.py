# -*- coding: utf-8 -*-
import pytest

from moneyed.classes import Money as M

from tax_calculator import calc


@pytest.mark.parametrize('inputs,expected_tax', [
    (
        {
            'country': 'GBR',
            'product_code': 'BREAD',
            'price': '2.50',
            'currency': 'GBP',
        },
        M('0.50', 'GBP')
    ),
    (
        {
            'country': 'GBR',
            'product_code': 'WINE75CL',
            'price': '5.00',
            'currency': 'GBP',
        },
        M('2.00', 'GBP')
    ),
    (
        {
            'country': 'GBR',
            'product_code': 'CIG',
            'price': '8.00',
            'currency': 'GBP',
        },
        M('2.00', 'GBP')
    ),
    # GER: The first €2 on all products is not taxable -> €6 taxable
    # GER: Tax on cigarettes is 30% -> €2.40
    (
        {
            'country': 'GER',
            'product_code': 'CIG',
            'price': '8.00',
            'currency': 'EUR',
        },
        M('1.8', 'EUR')
    ),
    # GER: The first €2 on all products is not taxable -> €6 taxable
    # Unknown products taxed at 10% -> €0.6
    (
        {
            'country': 'GER',
            'product_code': 'FAIL',
            'price': '8.00',
            'currency': 'EUR',
        },
        M('0.60', 'EUR')
    ),
    # GER: The first €2 on all products is not taxable -> €0 tax
    (
        {
            'country': 'GER',
            'product_code': 'FAIL',
            'price': '1.50',
            'currency': 'EUR',
        },
        M('0.00', 'EUR')
    ),
    # Unknown Countries should be taxed at 10%
    (
        {
            'country': 'FAIL',
            'product_code': 'CIG',
            'price': '8.00',
            'currency': 'EUR',
        },
        M('0.8', 'EUR')
    ),
    # Unknown UK products are taxed with VAT (20%), not 10%.
    (
        {
            'country': 'GBR',
            'product_code': 'FAIL',
            'price': '5.00',
            'currency': 'GBP',
        },
        M('1.00', 'GBP')
    ),
])
def test_calculate_tax(inputs, expected_tax):
    product, tax = calc.calculate_tax(**inputs)
    assert tax == expected_tax
