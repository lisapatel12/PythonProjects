#Lisa Patel (Driver)(U50140470) and Tianna Davis (Navigator)(U69901851)

#Slope of a Line
# Python program for slope of line 

x1=float(input("Enter the x-coordinate for point1: "))
y1=float(input("Enter the y-coordinate for point1: "))
x2=float(input("Enter the x-coordinate for point2: "))
y2=float(input("Enter the y-coordinate for point2: "))

#Calculate slope

slope=(y2-y1)/(x2-x1)

#print formatted slope
print("The slope for the line that connects two points ("+str(x1)+","+str(y1)+") and("+str(x2)+","+str(y2)+") is {:.5f}".format(slope))
