# -*- coding: utf-8 -*-
import click
from moneyed.classes import Money

from tax_calculator.catalogue import Catalogue


def calculate_tax(country, product_code, price, currency):
    price = Money(amount=price, currency=currency)
    tax = Money(amount='0', currency=currency)

    product = Catalogue.fetch(country, product_code)
    for rule in product.rules:
        tax_result = rule(price)
        if isinstance(tax_result, tuple):
            price = tax_result.next_amount
            tax += tax_result.tax
        else:
            tax += tax_result

    return tax


@click.command()
@click.argument('country', help='The country in which to apply the tax')
@click.argument('product code', help='A product code. e.g.: CIG')
@click.argument('price', help='Unitless price of the product')
@click.argument('currency', help='The currency used. e.g: GBP')
@click.option('--verbose', help='verbose')
def cli(country, product_code, price, currency):
    calculate_tax(country, product_code, price, currency)

if __name__ == '__main__':
    cli()
