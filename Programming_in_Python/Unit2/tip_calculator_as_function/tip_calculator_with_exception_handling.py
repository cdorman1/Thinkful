#!/usr/bin/python

import sys
from optparse import OptionParser
 
def calculate_rate(base, percentage):
    return base * percentage
 
def calculate_meal_cost(meal_base, tax_rate, tip_rate):
    """
    Calculates dollar amounts for tax, tip, and total meal cost
    """
    tax_value = calculate_rate(meal_base, tax_rate)
    meal_with_tax = tax_value + meal_base
    tip_value = calculate_rate(meal_with_tax, tip_rate)
    total = meal_with_tax + tip_value
    meal_info = dict(meal_base=meal_base,
                    tax_rate=tax_rate,
                    tip_rate=tip_rate,
                    tip_value=tip_value,
                    tax_value=tax_value,
                    total = total)
    return total_cost(meal_info)

def total_cost(meal_info):
    print "Cost of meal = ${0:.2f}".format(meal_info['meal_base'])
    print "Tax rate = {0}%".format(meal_info['tax_rate'])
    print "Tip rate = {0}%".format(meal_info['tip_rate'])
    print "Tip value = ${0:.2f}".format(meal_info['tip_value'])
    print "Tax value = ${0:.2f}".format(meal_info['tax_value'])
    print "Total = ${0:.2f}".format(meal_info['total'])
    
    

def main():
    args = [i for i in sys.argv[1:]]
    try:
        arg1 = int(args[0])
        arg2 = float(args[1])
        arg3 = float(args[2])
    except ValueError:
        print "Please enter the arguments as: integer float float(e.g., 20 .15 .20)"
        x = raw_input("Please enter total cost of meal, tax_rate, and tip_rate : " ).split(' ')
        x_arg1 = int(x[0])
        x_arg2 = float(x[1])
        x_arg3 = float(x[2])
        calculate_meal_cost(x_arg1, x_arg2, x_arg3)
    else:
        calculate_meal_cost(arg1, arg2, arg3)

if __name__ == '__main__':
    main()
