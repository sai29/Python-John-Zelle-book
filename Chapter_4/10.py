

import string

def main():
	message = raw_input("Enter the message: ")
	message1 = string.split(message)
	a = len(message1)
	print "The number of words in the message is", a

main()