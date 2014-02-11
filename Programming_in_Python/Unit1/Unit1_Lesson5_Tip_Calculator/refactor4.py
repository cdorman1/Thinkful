#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
Created on Fri Jan 03 17:33:32 2014

@author: cdorman
"""
from optparse import OptionParser


parser = OptionParser()

parser.add_option("-m", "--meal", dest = "meal", help = "Base cost of meal", type="float")
parser.add_option("-t", "--tax", dest = "tax_percent", help = "tax_percent", type="float")
parser.add_option("-p", "--tip", dest = "tip_percent", help = "percent tip you want to leave", type = "float", default = 0.15)

(options, args) = parser.parse_args()

if not (options.meal and options.tax_percent and options.tip_percent):
    parser.error("""
                Please provide the cost of your meal as -m (i.e. -m 20) without tax or tip.
                provide the tax amount in decimal form as -t (i.e. -t 0.15).
                provide the amount you would like to leave for a tip in decimal form as -p. 
                Note: if there is no value provided for tip a default of 0.15 will be used.
                """)
if not (options.meal):
    parser.error("Please provide the cost of your meal without tax and tip as -m")
if not (options.tax_percent):
    parser.error("Please provide the tax amount as a decimal -t")
if not (options.tip_percent):
    parser.error( "Please provide the tip amount as a decimal -p")


tax_value = options.meal * options.tax_percent
meal_with_tax = options.meal + options.meal * options.tax_percent
tip_value = meal_with_tax * options.tip_percent
total = meal_with_tax + tip_value


print "The base cost of your meal was $%.2f" % (options.meal)
print "You need to pay $%.2f for tax." % (tax_value)
print "Tipping at a rate of %.2f%%, you should leave $%.2f for a tip." % (options.tip_percent, tip_value)
print "The grand total of your meal is $%.2f." % (total)
