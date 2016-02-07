# -*- coding: utf-8 -*-
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
