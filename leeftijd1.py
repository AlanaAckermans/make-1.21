#!usr/bin/env python

#INFO
__author__ = "Alana Ackermans"
__version__ = "0.0.1"

#LIBRARIES



#FUNCTIONS
def geboortejaar():
    leeftijd = input("Hoe oud ben je?:")
    jaar = 2020
    vijftig = int(leeftijd) + 50
    a = int(jaar) - int(leeftijd)
    b = int(jaar)
    print("je bent geboren in: " , int(a))
    print ("binnen 50 jaar ben je: ", int(vijftig))

#MAIN FUNCTION
def main():
    geboortejaar()

#START PROGRAM
if __name__ == '__main__':
    main()