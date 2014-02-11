#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
Created on Fri Jan 03 17:33:32 2014

@author: cdorman
"""
from sys import argv

script, meal, tax, tip = argv

meal = float(meal) 
tax = float(tax)
tip = float(tip)


tax_value = meal * tax
meal_with_tax = meal + meal * tax
tip_value = meal_with_tax * tip
total = meal_with_tax + tip_value


print "The base cost of your meal was $%.2f" % (meal)
print "You need to pay $%.2f for tax." % (tax_value)
print "Tipping at a rate of %.2f%%, you should leave $%.2f for a tip." % (tip, tip_value)
print "The grand total of your meal is $%.2f." % (total)
