# -*- coding: utf-8 -*-
import pytest

from tax_calculator import calc


@pytest.mark.parametrize('inputs,tax', [
    ({'currency': 'GBP', 'product_code': 'BREAD', 'price': '2.50'}, 0.50),
    ({'currency': 'GBP', 'product_code': 'WINE75CL', 'price': '5.00'}, 2.00),
])
def test_calculate_tax(inputs, tax):
    assert calc.calculate_tax(**inputs) == tax
