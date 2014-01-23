def main():
    print "This program illustrates a chaotic function"
    x = input("Enter a number between 0 and 1: ")
    print "Index",x
    print "----------"
    for i in range(10):
    	print i,
        x = 3.9 * x * (1 - x)
        print "   ",x

main()