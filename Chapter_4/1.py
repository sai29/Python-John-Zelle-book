# Edit the numbers2text.py program to use a list to accept the ASCII code
# and append it to a list and join the strings in the list to get the code. 

import string 

def main():
    print "This program converts a sequence of ASCII numbers into"
    print "the string of text that it represents."
    print
    
    inString = raw_input("Please enter the ASCII-encoded message: ")

    message = []
    for numStr in string.split(inString):
        asciiNum = eval(numStr) 
        message1 = ord(asciiNum)          # convert digits to a number
        message.append(message1)

    print message
        
    print "The decoded message is:","".join(message)

main()
