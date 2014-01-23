def main():
	credit = int(raw_input("Enter the credits: "))
	if credit < 7:
		print "You are still a freshman"

	if credit > 7 and credit < 16:
		print "Sophmore you are"

	if credit > 16 and credit < 26:
		print "You are a junior"

	if credit > 26:
		print "Senior"
main()