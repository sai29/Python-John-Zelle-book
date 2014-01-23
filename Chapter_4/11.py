import string
def main():
	text = raw_input("Enter the text: ")
	text1 = string.split(text)
	a = len(text1)
	text2 = string.replace(text," ","")
	b = len(text2)
	c = (float(b)/a)
	print "The average number of words is", c

main()