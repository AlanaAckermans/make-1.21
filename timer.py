#!usr/bin/env python

#INFO
__author__ = "Alana Ackermans"
__version__ = "0.0.1"

#LIBRARIES
import time

#FUNCTIONS
def tijdsconvertie(sec):
    min = sec // 60
    sec = sec % 60
    uren = min // 60
    min = min % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(uren),int(min),sec))

def timer():
    input("druk op enter om te starten")
    start_tijd = time.time()
    input("druk op enter om te stoppen")
    eind_tijd = time.time()
    time_lapsed = eind_tijd - start_tijd
    tijdsconvertie(time_lapsed)

#MAIN FUNCTION
def main():
    timer()

#START PROGRAM
if __name__ == '__main__':
    main()