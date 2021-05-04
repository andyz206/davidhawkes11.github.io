"""
Program to caculate the area of triangle
"""

import math

def areaoftriangle():
    area=1/2 * B * H
    print("Returning area to main program")
    return(area)

B=float(input("What is the base of the triangle in cm?"))
H=float(input("What is the hieght of the triangle in cm?"))
print("The base and height of the triangle is",B ,"cm", H ,"cm")
print("Area is equal to",areaoftriangle(),"cm2")
