# -*- coding: utf-8 -*-
"""
Created on Fri Jan 03 17:33:32 2014

@author: cdorman
"""
meal = float(raw_input("Please provide the cost of your meal without tax or tip(i.e. 21.50): " )) 
tax = float(raw_input("Please provide the amount of tax as a decimal(i.e. 0.15): " ))
tip = float(raw_input("Please provide the amount of tip as a decimal(i.e. 0.15): " ))


tax_value = meal * tax
meal_with_tax = meal + meal * tax
tip_value = meal_with_tax * tip
total = meal_with_tax + tip_value


print "The base cost of your meal was $%.2f" % (meal)
print "You need to pay $%.2f for tax." % (tax_value)
print "Tipping at a rate of %.2f%%, you should leave $%.2f for a tip." % (tip, tip_value)
print "The grand total of your meal is $%.2f." % (total)
