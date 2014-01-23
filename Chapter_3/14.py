def main():
	try:
		n = int(raw_input("Enter the number of numbers: "))
		sum = 0
		for n in range(0,n):
			ip =int(raw_input("Enter the number: "))
			sum = sum + ip
			average = sum / n	
		
			print "The average is %d" %(average)
		
	except NameError:
		print "You did not enter the correct no of numbers"
	except TypeError:
		print "Your input were all not numbers"
    
    

main()


