#Lisa Patel (Driver)
### Finds the area of a Hexagon ###
import math

#gets side length
sideL = float(input("Enter the side length of your hexagon: "))

#calculates area
area = ((3*math.sqrt(3))/2)*math.pow(sideL,2)

#prints formated area (to 3 decimal places)
print( "The area of your hexagon is {:.3f}".format(area))
