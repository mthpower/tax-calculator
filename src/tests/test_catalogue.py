# -*- coding: utf-8 -*-

from tax_calculator import rules
from tax_calculator.catalogue import Catalogue, Product, default_product


def test_catalogue():
    assert Catalogue.fetch(
        country='GBR', product_code='BREAD'
    ) == ('Bread', rules.VAT)


def test_default_product():
    assert default_product() == Product(
        name='Unknown Product', rules=rules.DEFAULT)
