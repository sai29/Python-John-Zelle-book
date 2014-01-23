def main():
    print "This program calculates the future value"
    print "of a 10 year investment."

    principal = input("Enter the initial principal: ")
    apr = input("Enter the annualized interest rate: ")
    print "Year","Value"
    print "-----------"

    for i in range(10):
    	print i,
        principal = principal * (1 + apr)
        print "  ",principal

    print "The value in 10 years is:", principal

main()
