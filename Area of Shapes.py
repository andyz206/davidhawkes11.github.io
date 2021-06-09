import math

def areaofsquare():
     sidelength = float(input("What's the side length of your square in cm ? "))
     square = float(sidelength**2)
     print("The area of the square is",square,"cm2. ")

def areaofrectangle():
     length = float(input("What's the length of your rectangle in cm ? "))
     wide = float(input("What's the wide of your rectangle in cm ? "))
     rectangle = float(length*wide)
     print("The area of the rectangle is",rectangle,"cm2. ")

def areaoftriangle():
     base = float(input("What's the base length of your triangle in cm? "))
     height = float(input("What's the height of your triangle in cm? "))
     triangle = float(1/2*base*height)
     print("The area of the triangle is",triangle,"cm2.")
    
def areaofcircle():
     radius = float(input("What's the radius of your circle in cm ? "))
     degree = int(input("What's the degree of your circle in fraction? "))
     circle = float(degree*math.pi*radius**2)
     print("The area of the circle is",circle,"cm2.")

def areaofkite():
     x = float(input("What's the x diagonal of your kite in cm? "))
     y = float(input("What's the y diagonal of your kite in cm? "))
     kite = (1/2*x*y)
     print("The area of kite is",kite,"cm2.")

def trapezium():
     a = float(input("What's the base A of your trapezium in cm? "))
     b = float(input("What's the base B of your trapezium in cm? "))
     h = float(input("What's the height of your trapezium in cm? "))
     trapezium = float(a+b/2*h)
     print("The area of trapezium is",trapezium,"cm2.")

print("What shape's area do you want to caculate ? Select the following...")
print(">>> Square ")
print(">>> Rectangle ")
print(">>> Triangle ")
print(">>> Circle ")
print(">>> Kite ")
print(">>> Trapezium ")

choice = input("Choose one please. ")
if choice == "square":
     areaofsquare()
elif choice == "rectangle":
     areaofrectangle()
elif choice == "triangle":
     areaoftriangle()
elif choice == "circle":
     areaofcircle()
elif choice == "kite":
     areaofkite()
elif choice == "trapezium":
     areaoftrapezium()
else:
     print("That's invalid input ,please restart. ")
     
     
     
