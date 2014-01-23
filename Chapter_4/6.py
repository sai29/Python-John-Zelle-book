def main():

    name = raw_input("Enter your name: ").lower()

    letters = " abcdefghijklmnopqrstuvwxyz"
    value = 0
    for c in name:

        print c, letters.find(c) 
		value = letters.find(c) + value
	print "The numeric value of your name is", value
main()