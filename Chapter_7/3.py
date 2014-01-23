def main():
	mark = int(raw_input("Enter the marks: "))
	if mark > 89 and mark < 101:
		print "Your grade is A"
	if mark > 79 and mark < 90:
		print "Your grade is B"
	if mark > 69 and mark < 80:
		print "Your grade is C"
	if mark > 59 and mark < 70:
		print "Your grade is D"
	if mark < 60 :
		print "Your grade is E"
	else:
		print "Your mark is out of range"

main()

		