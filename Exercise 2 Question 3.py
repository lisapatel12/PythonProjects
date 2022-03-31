#Lisa Patel (Driver)(U50140470) and Shehryar Zaihd (Navigator)(U91165060)

#Input a temperature between -58F and 41F
ta = float(input("Enter the temperature in Fahrenheit between -58F and 41F: "))

#Confirmation of its boundaries
while ta > 41 or ta < -58:
    ta = float(input("Temperature must be between -58F and 41F\n Please re-enter the temperature in Fahrenheit: "))

#Input wind speed of greater than 2mph if temperature is within the boundaries
if ta < 41 and ta > -58:
    v = float(input("Enter the wind speed in miles per hour greater than 2 mph: "))

#Confirmation of wind speed and input windpeed again
while v < 2:
    v = float(input("Speed must be greater than or equal to 2\n Please re-enter the wind speed miles per hour: "))

#Final Calculation of wind chill index
if v >=2:
    twc=35.74 + (.6215 * ta) - (35.75 * (v**.16)) + (.4275 * ta * (v**.16))
print("The wind chill index is {:.3f}".format(twc))
