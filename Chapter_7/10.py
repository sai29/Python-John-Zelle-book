def main():
	year = int(raw_input("Enter the year: "))


	if year >= 1900 and year <= 2099 and year != 1954 and year != 1981 and year != 2049 and year != 2076:
		a = (year % 19 )
		b = (year % 4)
		c = (year % 7)
		d = (19 * a + 24) % 30
		e = (2*b + 4*c + 6*d + 5) % 7
		date = 22 + d + e
		date1 = d + e
		print date1
		if date1 < 9:
			print "Easter is on March %d" %(date)

		elif date1 > 9:
			date = 22 + d + e
			date2 = 31 - date
			print "Easter is on April %d" %(date2)
	else :
		a = (year % 19 )
		b = (year % 4)
		c = (year % 7)
		d = (19 * a + 24) % 30
		e = (2*b + 4*c + 6*d + 5) % 7
		date = 22 + d + e
		date1 = d + e
		print date1
		if date1 < 9:
			print "Easter is on March %d" %(date)

		elif date1 > 9:
			date = 22 + d + e
			date2 = 31 - date + 7
			print "Easter is on April %d" %(date2)

main()















