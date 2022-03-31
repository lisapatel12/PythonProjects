#Lisa Patel (Driver)

#list out the days 
days_week= ['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
week_sales= []

#create function to calculate the total sales of the week as well as avoid the negative values
for i in range(0,7):
    s = (int(input("Enter the sales for {}:".format(days_week[i]))))
    week_sales.append(s)
    if s<0:
        (float(input("Input was invalid. Re-enter the sales for {}:".format(days_week[i]))))
        week_sales.append(s)

#displays the total, minimum, and maximum amount
total = 0.0
for i in week_sales:
    total = total + i
print("The total sales is:$"+'{:.2f}'.format(total))
print("The minimum sale amount was:$"+ "{:.2f}".format(min(week_sales)))
print("The maximum sale amount was:$"+ "{:.2f}".format(max(week_sales)))
