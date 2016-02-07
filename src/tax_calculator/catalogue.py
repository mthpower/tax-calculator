from collections import namedtuple

from tax_calculator.rules import UK_WINE, VAT

Product = namedtuple('Product', ['name', 'rules'])

CATALOGUE = {
    'BREAD': Product(name='Bread', rules=VAT),
    'WINE75CL': Product(name='Wine - 75cL', rules=UK_WINE),
}


class Catalogue(object):

    catalogue = CATALOGUE

    @classmethod
    def fetch_by_code(cls, product_code):
        return cls.catalogue[product_code]
