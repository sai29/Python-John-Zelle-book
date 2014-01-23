import math

def main():
	x = float(raw_input("Enter the number: "))
	guess = x / 2
	guess1 = nextGuess(guess,x)
    
	print "The square root is", guess1

def nextGuess(guess,x):
	g = int(raw_input("Enter the number of iterations: "))
	for i in range(g):
		guess = (guess + (x/guess))/2
	
	diff = math.sqrt(x)- guess
	print "The difference is", diff
	return guess
	

main()