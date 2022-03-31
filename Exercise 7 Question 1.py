#Driver:Lisa Patel
#We are creating a program that collects information from the user abou the pet .
#The program has a default of 0 age and unprovided name and type of the pet
#The user then enters the pet's age ,name ,and type 

print('A pet object has been created. Here is the initial information about the pet: ')#first print statement related to the default 


class Pet: #creating a class called "pet" and initializing it with values zero for each attribute
    def __init__(self):
        self.__nameofthepet = 0
        self.__typeofthepet = 0
        self.__ageofpet = 0

    def setnameofthepet(self , nameofthepet):#setter method for name 
        self.__nameofthepet = nameofthepet

    def settypeofthepet(self , typeofthepet):#setter method for type
        self.__typeofthepet = typeofthepet

    def setageofpet(self , ageofpet):#setter method for age
        self.__ageofpet = ageofpet

    def getnameofthepet(self):#getter method for name
        return self.__nameofthepet

    def gettypeofthepet(self):#getter method for type 
        return self.__typeofthepet

    def getageofpet(self):#getter method for age
        return self.__ageofpet




def main():#main function in the program
    print('Name of pet:  Not provided')
    print('Type of pet:  Not provided')
    print('Age of pet:  0')
    print("Let's update the information for a pet!")

    name = input("Enter the pet's name:" )#assigning variable for name user input
    species = input('Enter the type of animal:')#assigning variable for type user input
    age = int(input("Enter the pet's age :"))#asiigning variable for age user input)

    info = Pet()#automatically call __init__ method

    info.setnameofthepet(name)#mutator for the user entered name
    info.settypeofthepet(species)#mutator for user entered type 
    info.setageofpet(age)#mutator for the user entered age

    print('Here is the updated information about the pet: ')#first print statement of the updated information

    print('Name of pet: {}'.format(info.getnameofthepet()))# printing the new name using accessor methods
    print('Type of pet: {}'.format(info.gettypeofthepet()))# printing the new type using accessor methods
    print('Age : {}'.format(info.getageofpet())) # printing the new age using accessor methods


main() #calling the main function
