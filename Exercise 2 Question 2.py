# Driver: Shehryar Zaihd U91165060
# Navigator: Lisa Patel U50140470
# Assignment 2 Perimeter of a triangle

# Program Description: Program prompts user for lengths of a triangle and computes the perimeter if the input is valid.
# Otherwise program outputs message stating that the input is invalid.

# statements for input of length
length_1= float(input('Please enter the length of side 1 : '))
print() # adds new line to make the program look cleaner
length_2= float(input('Please enter the length of side 2 : '))
print()
length_3= float(input('Please input the length of side 3 : '))
print()

# condition statement to validate lengths
if length_1+length_2 > length_3 and length_1+length_3 > length_2 and length_3+length_2 > length_1:
    perimeter = length_1 + length_2 + length_3 
    print("The perimeter of the triangle is ", perimeter, " units.",sep='')

# else statement fot false inputs
else :
    print("Perimeter cannot be calculated: the input is invalid.")
