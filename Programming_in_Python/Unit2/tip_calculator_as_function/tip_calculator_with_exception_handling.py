import sys
from optparse import OptionParser
 
def calculate_rate(base, percentage):
    return base * percentage
 
def calculate_meal_costs(meal_base, tax_rate, tip_rate):
    """
    Calculates dollar amounts for tax, tip, and total meal cost
    """
    tax_value = calculate_rate(meal_base, tax_rate)
#    print tax_value
 #   sys.exit()
    meal_with_tax = tax_value + meal_base
    tip_value = calculate_rate(meal_with_tax, tip_rate)
    total = meal_with_tax + tip_value
    meal_info = dict(meal_base=meal_base,
                    tax_rate=tax_rate,
                    tip_rate=tip_rate,
                    tax_value=tax_value,
                    total = total)
    print meal_info

def main():
    args = [i for i in sys.argv[1:]]
    calculate_meal_costs(int(args[0]), float(args[1]), float(args[2]))

if __name__ == '__main__':
    main()
