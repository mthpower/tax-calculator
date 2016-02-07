# -*- coding: utf-8 -*-
"""
A Tax Calulator.

This module contains the CLI entry point to the tax calculator, using the
brilliant `click` module from Armin Ronacher.

The tax calculator has the slightly convoluted logic of dealing with both
the possible return types of the rules. I can see simplifing all the rules
to return a TaxResult being a good move that would simplify the code here.
At the time of writing I wanted to keep the interface of the simpler rules
(e.g.: `flat` and `percent`) as simple as possible.

I haven't explored the behaviour of the Money class and my code with negative
amounts fully, or pushed the edge cases much. If it isn't in the tests, I
didn't try it.
"""
import click
from moneyed.classes import Money

from tax_calculator.catalogue import Catalogue

TEMPLATE = (
    'Tax on {product.name} worth {price} in {country} is '
    '{tax.amount} {tax.currency}'
)


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

    return product, tax


@click.command()
@click.argument('country')
@click.argument('product')
@click.argument('price')
@click.argument('currency')
@click.option('--verbose', help='verbose', is_flag=True)
def cli(country, product, price, currency, verbose):
    product, tax = calculate_tax(country, product, price, currency)
    if not verbose:
        print(tax.amount, tax.currency)
    else:
        print(TEMPLATE.format(
            product=product, price=price, country=country, tax=tax
        ))

if __name__ == '__main__':
    cli()
