#Lisa Patel (Driver)

#Runway Length
#getting take-off speed from the user
v=float(input("Enter the take-off speed in m/s: "))

# getting the airplane acceleration from the user
a=float(input("Enter the airplane's acceleration in m/s**2: "))

#calculating the runway length using the given formula
length=(v*v)/(2* a)

#displaying the runway length
print("The minimum runway length needed for this airplane is %.4f meters." % length)
