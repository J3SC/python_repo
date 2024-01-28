#!/usr/bin/env python3

weight = input ("Weight: ")
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = int(weight) / 0.45
    print ("Weight in Lbs: " + str(converted))
elif unit.upper() == "L":
    converted = int(weight) * 0.45
    print("Weight in Kg: " + str(converted))




