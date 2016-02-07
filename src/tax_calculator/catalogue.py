# -*- coding: utf-8 -*-
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
