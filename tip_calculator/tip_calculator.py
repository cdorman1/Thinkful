# -*- coding: utf-8 -*-
"""
Created on Fri Jan 03 17:33:32 2014

@author: cdorman
"""
meal = 20
tax = 0.15
tip = 0.15

tax_value = meal * tax
meal_with_tax = meal + meal * tax
tip_value = meal_with_tax * tip
total = meal_with_tax + tip_value


print "The base cost of your meal was $%s" % ("{0:.2f}".format(meal))
print "You need to pay $%s for tax." % ("{0:.2f}".format(tax_value))
print "Tipping at a rate of 15%%, you should leave $%s for a tip." % ("{0:.2f}".format(tip_value))
print "The grand total of your meal is $%s." % ("{0:.2f}".format(total))

#python tip_calculator.py
#The base cost of your meal was $20.00
#You need to pay $3.00 for tax.
#Tipping at a rate of 15%, you should leave $3.45 for a tip.
#The grand total of your meal is $26.45.


