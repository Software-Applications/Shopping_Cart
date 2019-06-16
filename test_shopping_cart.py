# pytest script for automated test

import pytest
import datetime
from shopping_cart import *



def test_to_usd():
    assert to_usd(5) == "$5.00"
    assert to_usd(0.26) == "$0.26"
    assert to_usd(4.2) == "$4.20"
    assert to_usd(1000) == "$1,000.00"

def test_calc_tax():
    assert calc_tax(100) == 8.75
    assert calc_tax(0) == 0

def test_calc_total_bill_amt():
    assert calc_total_bill_amt(100) == 108.75
    assert calc_total_bill_amt(156) == 169.65
    assert calc_total_bill_amt(0) == 0

def test_def_date():
    now = datetime.datetime.now()
    assert def_date() == now.strftime("%Y-%m-%d:%I:%M:%S %p")

def test_validate_prod():
    assert validate_prod("5", [0,1,2,3,4,5]) == None
    assert validate_prod("6", [0,1,2,3,4,5]) == None
    assert validate_prod("5", ['0','1','2','3','4','5']) == '5'
    assert validate_prod("6", ['0','1','2','3','4','5']) == None
    assert validate_prod("Done") == "done"