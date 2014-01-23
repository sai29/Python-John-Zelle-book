def main():
	year = int(raw_input("Enter the year: "))
	month = int(raw_input("Enter the month: "))
	date = int(raw_input("Enter the date"))
	if year >= 1:
		print "Its a legal year"
		if month <= 12 and month >= 1:
			print "Its a legal month"
			if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or  month == 12:
				if date >= 1 and date <= 31:
					print "Its a legal date."
				else:
					print "Its not a legal date"
			elif month == 4 or month == 6 or month == 9 or month == 11:
				if date >= 1 and date<= 30:
					print "Its a legal date"
				else:
					print "Its not a legal date."
			elif month == 2:
				if date >= 1 and date <= 28 and year % 4 != 0:
					print "Its a legal date"
				elif date >= 1 and date <= 28 and year % 4 == 0 and year % 100!= 0:
					print "Its a legal date and a leap year"
				elif date >=1 and date <= 29 and year % 4 == 0 and year % 400 == 0:
					print "Its a legal date"
				else:
					print "Its not a legal date."
		else:
			print "Its not a legal month"
	else:
		print "Its not a legal year"

main()