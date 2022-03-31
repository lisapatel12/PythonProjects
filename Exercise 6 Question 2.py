#Lisa Patel (Navigator) U50140470
#Olivia Santana-Arellano (Driver) U58327253
#This program uses a dictionary to encrypt a text file and provides output.

#creating dictionary
def encryption(codes):
    filename = input('Enter the name of the input file (with extension):')
    
    #open a file for reading
    original = open(filename, 'r') #r - mode for reading a file
    original_file = original.read()
    

    #Open file for encrypted message
    efilename = input('Enter the name of the output file (with extension):')
    encrypted_file = open(efilename,'w')

    #read contents
    for character in original_file:
        if character in codes:
            encrypted_file.write(codes[character])
            print(character, end='')
        else:
            encrypted_file.write(character)
            print(character, end='')


    #close the file
    encrypted_file.close()

def main():
    codes = {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8',\
            'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',\
            'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',\
            'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',\
            'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v',\
            'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',\
            'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p',\
            'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m',\
            'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',\
            '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g',\
            '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d',\
            '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a',\
            ':':',',',':':','?':'.','.':'?','<':'>','>':'<',\
            "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=',\
            '{':'[','[':'{','}':']',']':'}'}

    encryption(codes)
    
main()
