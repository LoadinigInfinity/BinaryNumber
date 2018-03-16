#-------------------------------------------------------------------------------
# Name:     binaryNumber_driver.py
# Purpose:  Rudimentary interactive testing for the BinaryNumber class.
#
# Author:      nakazawam and pearcej
#
# Created:     21/09/2014
# Corrected conversion to Python 3.0 16/03/2018
#-------------------------------------------------------------------------------

from  binaryNumber import BinaryNumber

def main():
    testing = BinaryNumber() # instantiation of testing list.
    tobeconverted = input("Please enter the integer that you want to convert: ")
    testing.convert_decimal_to_binary(int(tobeconverted))
    print(testing)
    print("converted " + tobeconverted + " to binary.")
    testing.increment()
    print(testing)
    print("after incrementing (needs to be implemented.)")
    testing.remove_all()
    print(testing)

if __name__ == '__main__':
    main()
