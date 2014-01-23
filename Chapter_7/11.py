def main():
	year = int(raw_input("Enter the year: "))
	if year % 4 == 0 and year % 100 != 0:
		print "Its a leap year"

	elif year % 4 == 0 and year % 400 == 0:
		print "Its a leap year"

	else:
		print "Its not a leap year"

main()

