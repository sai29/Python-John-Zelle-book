def main():
	number = int(raw_input("Enter the number"))
	sum1 = sumN(number)
	sum2 = sumNcubes(number)
	print "The sum of the numbers is", sum1
	print "The sum of the cubes of the numbers is", sum2

def sumN(n):
	sum = 0
	for i in range(1,n+1):
		sum = sum + i
	return sum

def sumNcubes(n):
	sum = 0
	for i in range(1,n+1):
		sum = sum + (i*i*i)
	return sum

main()