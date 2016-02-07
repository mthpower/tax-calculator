# -*- coding: utf-8 -*-
from moneyed.classes import Money

from tax_calculator.catalogue import Catalogue


def calculate_tax(country, product_code, price, currency):
    price = Money(amount=price, currency=currency)
    tax = Money(amount='0', currency=currency)

    product = Catalogue.fetch(country, product_code)
    for rule in product.rules:
        tax_result = rule(price)
        if isinstance(tax_result, tuple):
            price = tax_result.next_price
            tax += tax_result.tax
        else:
            tax += tax_result

    return tax
