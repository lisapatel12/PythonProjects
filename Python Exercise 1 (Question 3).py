#Lisa Patel (Driver)
### Tip Calculator ###

#variable assignment
subtotal = int(input("Enter the subtotal: $"))
tip = int(input("Enter tip: %"))
tip = tip/100

#calculates the total
print() 
total = (subtotal*tip) + subtotal

#prints the info in a formatted way
print ("""~RECEIPT~
Subtotal: ${:,.2f}
Tip: {:.0%}
-----
Total: ${:,.2f}

Have a nice day :)""".format(subtotal, tip, total))
