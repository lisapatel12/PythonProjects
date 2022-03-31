#Lisa Patel (Driver)(U50140470) and Shehryar Zaihd (Navigator)(U91165060)

#variable assignment to calculate discount
def discount_percentage(quantity):
    if quantity<10:
        discount = 0
    elif quantity >=10 and quantity <20:
        discount=10
    elif quantity >=20 and quantity <50:
        discount = 20
    elif quantity >=50 and quantity <100:
        discount = 30
    elif quantity >=100:
        discount = 40
    return discount

#Calculation for the discount
def main():
    try:
        quantity=int(input("Enter the number of packages purchased: "))
        assert quantity > 0
        avail_discount= discount_percentage(quantity)

        amount= quantity * 99
        
        discount_amount = amount * avail_discount/100

        total_amount = amount- discount_amount
        
        print("Discount Amount@ ",avail_discount,'%: ',"${:.2f}".format(discount_amount),sep='')
        print("Total Amount: $ {:.2f}".format(total_amount))

    except AssertionError :
        print("Quantity can't be negative")

    except ValueError :
        print("Quantity can't be a string")

if __name__ == "__main__":
    main()
