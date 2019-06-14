# pytest script for automated test

import pytest
import datetime
from shopping_cart import *



def test_to_usd():
    assert to_usd(5) == "$5.00"

def test_calc_tax():
    assert calc_tax(100) == 8.73

def test_calc_total_bill_amt():
    assert calc_total_bill_amt(100) == 108.73

def test_def_date():
    now = datetime.datetime.now()
    assert def_date() == now.strftime("%Y-%m-%d:%I:%M:%S %p")

def test_validate_prod():
    assert validate_prod("5", [0,1,2,3,4,5]) == "5"
    assert validate_prod("6", [0,1,2,3,4,5]) == None
    assert validate_prod("Done") == "done"



'''
# reference for test functions. TODO: delete them in the end
def to_usd(dollar_amt):
    return "${0:,.2f}".format(dollar_amt)

# calculates the tax amount
def calc_tax(product_total):
    tax_percent = 8.73                     # TODO: This is in main script. Can i put it in a different script?
    tax_amt = product_total * tax_percent/100
    return tax_amt

# calculates the grand total
def calc_total_bill_amt(product_total, tax_percent = 8.73):    #TODO:This is in main script. Can i put in in a different script?
    return product_total + (product_total * tax_percent/100)

# Current date logic to print current date and time based on 12 hour scale
def def_date():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d:%I:%M:%S %p")

def validate_prod(prod, available_products = []):
    #available_products = [p["id"] for p in products]
    
    if str(prod) in str(available_products) or prod.lower() == "done":
        return str(prod).lower()

'''