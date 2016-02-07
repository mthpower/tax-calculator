# -*- coding: utf-8 -*-
from moneyed.classes import Money as M

from tax_calculator import rules


def test_percent():
    assert rules.percent(M('100.0'), '0.5') == M('0.5')
    assert rules.percent(M('100.0'), '20') == M('20.0')
    assert rules.percent(M('100.0'), '110') == M('110.0')


def test_flat():
    assert rules.flat(M('123'), M('2')) == M('2.0')


def test_tax_band():
    assert rules.tax_band(M('100'), M('-2')) == rules.TaxResult(
        tax=M('0'), next_price=M('98'))
