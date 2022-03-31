#Lisa Patel (Driver)

#make it accept the text file and convert into pig latin
file= open('phrase.txt', 'w')
file.write('I slept most of the night')
file.close()
fileopen = open('phrase.txt', 'r')
phrase=fileopen.read()
fileopen.close()

#input the phrase and write the results 
phrase = phrase.split()

for i in range(len(phrase)):
    word= phrase[i]
    letter_one= word[0]
    word=list(word)
    word.remove(letter_one)
    word.append(letter_one)
    word.append('a')
    word.append('y')
    word="".join(word)
    phrase[i]= word
    

#translated text    
phrase= " ".join(phrase)
print (phrase)

file= open('phrase.txt', 'w')
file.write(phrase)
file.close()
    
    
               
