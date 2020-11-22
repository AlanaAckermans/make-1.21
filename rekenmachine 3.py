#!usr/bin/env python

#INFO
__author__ = "Alana Ackermans"
__version__ = "0.0.1"

#LIBRARIES

#FUNCTIONS
def rekenmachine():
    a = input("kies een getal")
    b = input("kies nog een getal")
    totaal = (int(a) + int(b))
    print("het opgetelde van deze cijfers is:" , int(totaal))

#MAIN FUNCTION
def main():
    rekenmachine()

#START PROGRAM
if __name__ == '__main__':
    main()