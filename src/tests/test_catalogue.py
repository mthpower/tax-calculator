# -*- coding: utf-8 -*-

from tax_calculator import rules
from tax_calculator.catalogue import Catalogue


def test_catalogue():
    assert Catalogue.fetch_by_code('BREAD') == ('Bread', rules.VAT)
