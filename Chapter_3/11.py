def main():
	n = int(raw_input("Enter the number of numbers: "))
	sum = 0
	for n in range(0,n+1,1):
		sum = sum + n
		
	print "The sum is %d" %(sum)
		

    

main()