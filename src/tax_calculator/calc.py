# -*- coding: utf-8 -*-
from tax_calculator.catalogue import Catalogue


def calculate_tax(currency, product_code, price):
    product = Catalogue.fetch_by_code(product_code)
    return product.rules(price)
