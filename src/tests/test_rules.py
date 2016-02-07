# -*- coding: utf-8 -*-
from tax_calculator import rules


def test_percent():
    assert rules.percent('100.0', '0.5') == 0.5
    assert rules.percent('100.0', '20') == 20.0
    assert rules.percent('100.0', '110') == 110.0


def test_vat():
    assert rules.VAT('100.0') == 20.0
