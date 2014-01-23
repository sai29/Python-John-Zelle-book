def main():
	n = int(raw_input("Enter the number of numbers: "))
	sum = 0
	for n in range(0,n):
		ip =int(raw_input("Enter the number: "))
		sum = sum + ip
		
	print "The sum is %d" %(sum)
main()