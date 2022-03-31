# Driver: U50140470
# Assignment 2 Ramp angle

# Program Description:
# Program prompts the user for mass and force as input and
# calculates and outputs the angle

import math # importing math module for access to asin and degrees functions

small_g = 9.8
"""creating constant small_g for acceleration due to gravity,
which is 9.8 m/s^2"""

# getting inputs from user for mass of the cart and force exerted 
mass= float(input('Please enter the mass of the cart in kilograms : '))
print() # adding a line just to make it look a little nicer
force=float(input('Please enter the force in Newtons : '))
print()
# calculating the angle and converting it to degrees
theta = math.asin((force/(mass*small_g)))
theta = math.degrees(theta)

#  printing the end result for the user
print("The angle of the ramp is" ,'{:.1f}'.format(theta), "degrees")


