import math
def main():
	no = int(raw_input("Enter the number: "))
	no1 = math.sqrt(no)
	print no1
	no2 = int(no1)
	print no2
	for i in range(2,no2,1):
		val = no % no2
		if val == 0:
			print "The value is not prime"
			break
		else:
			no2 = no2-1
		if no2 == 2:
			print "The number %d is a prime number." %(no)



main()
