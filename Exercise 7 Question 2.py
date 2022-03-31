#Lisa Patel (Driver)
class RetailItem:
    def __init__(self,itemType,amount,price):
#put the data items out and declare it
        self._itemType = itemType
        self._amount = amount
        self._price = price

    def __str__(self):
#str() function
        out = '{:<20}{:<10}${:<10.2f}'.format(self._itemType,
                                            str(self._amount),
                                            self._price)
#returning the formatted string
        return out

def main():
#put in the details the the first item
    name = input('Name of item 1: ')
    amount = int(input('Amount of item 1: '))
    price = float(input('Price of item 1: '))
    item1 = RetailItem(name,amount,price)
    
#put in the details the the second item
    
    name = input('Name of item 2: ')
    amount = int(input('Amount of item 2: '))
    price = float(input('Price of item 2: '))
    item2 = RetailItem(name,amount,price)

#print the final table
    
    print("Here is a summary of the items you added:")
    print('{:<20}{:<10}{:<10}'.format('Item',
                                        'Amount',
                                        'Price'))
    print('-------------------------------------------------')
    print(item1)
    print(item2)
#call main back
main()
