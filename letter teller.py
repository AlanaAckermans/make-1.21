#!usr/bin/env python

#INFO
__author__ = "Alana Ackermans"
__version__ = "0.0.1"

#LIBRARIES

#FUNCTIONS
def teller():
    a = input("Kies een woord")
    print("Jouw woord heeft:" , len(a) , "letters")

#MAIN FUNCTION
def main():
    teller()

#START PROGRAM
if __name__ == '__main__':
    main()