import math
def main():
	no = int(raw_input("Enter the number: "))
	no1 = math.sqrt(no)
	no2 = int(no1)
	while True:
		for i in range(2,no2,1):
			val = no % no2
			if val != 0:
				no2 = no2 -1
			if no2 < 2:
				print "The number %d is a prime number." %(no)
		no = no - 1
		if no == 1:
			break






main()
