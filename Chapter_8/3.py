def main():
	interest = float(raw_input("Enter the interest rate: "))
	amount = int(raw_input("Enter the amount: "))
	year = 0
	interest1 = interest / 100
	new_amount = 2 * amount
	while amount <= new_amount:
		amount = amount * (1 + interest1)
		year = year + 1


	print "The number of year the investment takes to double is %d" %(year)


main()