# -*- coding: utf-8 -*-
from tax_calculator.catalogue import Catalogue


def calculate_tax(country, product_code, price):
    product = Catalogue.fetch(country, product_code)
    return product.rules(price)
