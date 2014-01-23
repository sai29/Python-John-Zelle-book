import math
def main():
	x = float(raw_input("Enter the number: "))
	n = int(raw_input("Enter the number of guesses: "))
	guess = x / 2
	for i in range(0,n):
		guess = ((guess + (x / guess))/2)

	print "The guess is %f" %(guess)
	diff = math.sqrt(x)- guess
	print "The diff is %f" %(diff)
main()
