from collections import defaultdict, namedtuple

from tax_calculator import rules

Product = namedtuple('Product', ['name', 'rules'])


def default_product():
    return Product(name='Unknown Product', rules=rules.DEFAULT)


def country(dict_):
    return defaultdict(default_product, dict_)


UK_CATALOGUE = {
    'BREAD': Product(name='Bread', rules=rules.VAT),
    'WINE75CL': Product(name='Wine - 75cL', rules=rules.UK_WINE),
    'CIG': Product(name='Cigarettes', rules=rules.UK_CIG),
}

GER_CATALOGUE = country({
    'CIG': Product(name='Cigarettes', rules=rules.GER_CIG),
})


class Catalogue(object):

    catalogues = {
       'GBR': UK_CATALOGUE,
       'GER': GER_CATALOGUE,
    }

    @classmethod
    def fetch(cls, country, product_code):
        country_cat = cls.catalogues[country]
        return country_cat[product_code]
