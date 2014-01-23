# A certain CS professor gives 100-point exams that are graded on the scale
# 90 -
# cepts an exam score as input and prints out the corresponding grade.

def main():
	mark = int(raw_input("Enter the mark: "))

	if mark in range(0,60):
		print "Your grade is F"

	if mark in range(60,70):
		print "Your grade is D"

	if mark in range(70,80):
		print "Your grade is C"

	if mark in range(80,90):
		print "Your grade is B"

	if mark in range(90,101):
		print "Your grade is A"

main()

