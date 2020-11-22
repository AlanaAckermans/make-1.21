#!usr/bin/env python

#INFO
__author__ = "Alana Ackermans"
__version__ = "0.0.1"

#LIBRARIES

#LISTS
bands = ["joy division", "metallica", "iron maiden"]

#FUNCTIONS
def toevoegen():
    print(bands)
    band_a = input("type een band om toe te voegen aan deze lijst")
    bands.append(band_a)  # adding the element
    print(bands)

#MAIN FUNCTION
def main():
    toevoegen()

#START PROGRAM
if __name__ == '__main__':
    main()