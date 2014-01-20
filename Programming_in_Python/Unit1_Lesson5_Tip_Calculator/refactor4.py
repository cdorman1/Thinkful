#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
Created on Fri Jan 03 17:33:32 2014

@author: cdorman
"""
from optparse import OptionParser


parser = OptionParser()

parser.add_option("-m", "--meal",  dest="first_arg", help="Please provide the cost of your meal without tax and tip",
                    type="float")
parser.add_option("-t", "--tax", dest="second_arg", help="Please provide the tax amount as a decimal", 
                    type="float")
parser.add_option("-p", "--tip", dest="third_arg", help="Please provide the tip amount as a decimal",
                    type="float", default=0.15)

(options, args) = parser.parse_args()

if not (options.first_arg and options.second_arg and options.third_arg):
    parser.error("""Please provide the cost of your meal as -m without tax or tip
                provide the tax amount in decimal form as -t
                provide the amount you would like to leave for a tip as -p Note: if there is no value
                provided for tip a default of 0.15 will be used.
                """)
if not (options.first_arg):
    parser.error("Please provide the cost of your meal without tax and tip as -m")
if not (options.second_arg):
    parser.error("Please provide the tax amount as a decimal -t")
if not (options.third_arg):
    parser.error( "Please provide the tip amount as a decimal -p")


meal = (options.first_arg) 
tax = (options.second_arg)
tip = (options.third_arg)


tax_value = meal * tax
meal_with_tax = meal + meal * tax
tip_value = meal_with_tax * tip
total = meal_with_tax + tip_value


print "The base cost of your meal was $%.2f" % (meal)
print "You need to pay $%.2f for tax." % (tax_value)
print "Tipping at a rate of %.2f%%, you should leave $%.2f for a tip." % (tip, tip_value)
print "The grand total of your meal is $%.2f." % (total)
