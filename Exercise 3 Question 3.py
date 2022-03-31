#Morse Code Converter
#Lisa Patel (Driver)
#This program is meant for the user to enter a string and it will convert it to Morse code sequencing

#Creating a dictionary to store the store alphabet and other common puncuations to compare to the
#morse code
text = [',','.','?','0','1','2','3','4','5','6','7','8','9'
        ,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o'
        ,'p','q','r','s','t','u','v','w','x','y','z']

#Creating a dictionary of the sequence in Morse code to correlate to the text of the alphabet
morsecode = ['--..--','.-.-.-','..--..','-----','.----','..---','...--','....-','.....','-....','--...','---..','----.'
             ,'.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.'
             ,'---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']

#Output to store the string in string
string = input("Enter the string to be converted to Morse code : ")

#Conversion of the string to all lowercase
string = string.lower()

#For loop to determine whether what is entered is in the text then it is put into the if statement
#to determine to print a assigned value for that entry or not
for n in string:
    if n == ' ':
        print(end= " ")
    if n in text:
        print(morsecode[text.index(n)], end= "")

