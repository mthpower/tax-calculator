# -*- coding: utf-8 -*-
"""
A Product Catalogue.

Tax is calculated by looking up the product code in the country's product
catalogue. At present, these have to be be build per country, and map product
codes to namedtuple instances that have rules. Rules is expected to a be a list
of callable tax rules. Ordering is important, as it allows the specification of
tax laws such as "The first €2 on all products is not taxable".

Defaults are set up if the Product or Country is not known.

I chose to stick with implementing the countries and their tax rules in
standard data types with some help from `collections. After a certain point
this approach will begin to show it's limitations. A heuristic for this will
be when structures that mimic Foreign Keys start to show up. This is a good
time to move to a different data model.

At the moment, I don't have a nice way to say "Apply this rule to all products
of a country" which is a limitation.

A further limitation is that groups of products are not implemented, just a
straightforward lookup from product code -> product -> rules.
"""
from collections import defaultdict, namedtuple

from tax_calculator import rules

Product = namedtuple('Product', ['name', 'rules'])


def default_product():
    return Product(name='Unknown Product', rules=[rules.TEN_PC])


def country(dict_):
    return defaultdict(default_product, dict_)


def GER_default_product():
    return Product(
        name='Unknown Product', rules=[rules.DEDUCT_TWO_EUR, rules.TEN_PC]
    )


def GBR_default_product():
    return Product(name='Unknown Product', rules=[rules.VAT])


GBR_CATALOGUE = defaultdict(GBR_default_product, {
    'BREAD': Product(name='Bread', rules=[rules.VAT]),
    'WINE75CL': Product(name='Wine - 75cL', rules=[rules.GBR_WINE]),
    'CIG': Product(name='Cigarettes', rules=[rules.TWENTY_FIVE_PC]),
})

GER_CATALOGUE = defaultdict(GER_default_product, {
    'CIG': Product(
        name='Cigarettes',
        rules=[rules.DEDUCT_TWO_EUR, rules.THIRTY_PC]
    ),
})


class Catalogue(object):

    catalogues = {
       'GBR': GBR_CATALOGUE,
       'GER': GER_CATALOGUE,
    }

    @classmethod
    def fetch(cls, country_code, product_code):
        try:
            country_cat = cls.catalogues[country_code]
        except KeyError:
            country_cat = country({})

        return country_cat[product_code]
