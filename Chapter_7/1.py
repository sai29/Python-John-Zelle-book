def main():
	work = int(raw_input("Enter the number of hours: "))
	if work < 40:
		print "Your pay is %d" %(work)
	else:
		pay = work * 1.5
		print "Your pay is %d" %(pay)

main()
