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
					dnum(year,month,date)
				else:
					print "Its not a legal date"
			elif month == 4 or month == 6 or month == 9 or month == 11:
				if date >= 1 and date<= 30:
					print "Its a legal date"
					dnum(year,month,date)
				else:
					print "Its not a legal date."
			elif month == 2:
				if date >= 1 and date <= 28 and year % 4 != 0:
					print "Its a legal date"
					dnum(year,month,date)				
				if date >= 1 and date <= 29 and year % 4 == 0 and year % 100!= 0:
					print "Its a legal date."
					dnum(year,month,date)
				elif date >=1 and date <= 29 and year % 4 == 0 and year % 400 == 0:
					print "Its a legal date"
					dnum(year,month,date)
				else:
					print "Its not a legal date."
		else:
			print "Its not a legal month"
	else:
		print "Its not a legal year"

def dnum(year,month,date):
	if year % 4 == 0 and year % 100 != 0:
		print "Its a leap year"
		if month == 1 or month == 2:
			daynum = 31 *(month - 1) + date  
			print "The day number is %d" %(daynum)
		else:
			daynum = 31 *(month - 1) + date + 1
			daynum1 = ((4 * month) + 23) / 10
			daynum3 = (daynum - daynum1)
			print "The day number is %d" %(daynum3)

	elif year % 4 == 0 and year % 400 == 0:
		print "Its a leap year"
		if month == 1 or month == 2:
			daynum = 31 *(month - 1) + date  
			print "The day number is %d" %(daynum)
		else:
			daynum = 31 *(month - 1) + date + 1
			daynum1 = ((4 * month) + 23) / 10
			daynum3 = (daynum - daynum1)
			print "The day number is %d" %(daynum3)
	else:
		print "Its not a leap year"
		if month == 1 or month == 2:
			daynum = 31 *(month - 1) + date  
			print "The day number is %d" %(daynum)
		else:
			daynum = 31 *(month - 1) + date 
			daynum1 = ((4 * month) + 23) / 10
			daynum3 = (daynum - daynum1)
			print "The day number is %d" %(daynum3)

main()




S