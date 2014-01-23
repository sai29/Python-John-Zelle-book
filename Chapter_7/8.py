def main():
	age = int(raw_input("Enter the age: "))
	if age < 25:
		print "You are not eligible since you are not atleast 25 years of age."
	if age >= 25:
		ques = str(raw_input("If you are a US born citizen press 1 or if naturalized press 2: "))
		if ques == "1":
			if age >= 30:
				print "You are eligible to run for both the Senate and the House!"

			elif age >= 25 and age < 30:
				print "You are eligible to run for the House only.!"

		elif ques == "2":
			age1 = int(raw_input("Enter the year in which you got your citizenship: "))
			diff = 2013 - age1
			if diff >= 7 and age >= 30:
				print "You are eligible to run for both the Senate and the House!"

			if diff >= 7 and age >= 25 and age < 30:
				print "You are eligible to run for the house!"

			if diff < 7:
				print "You are not eligible."
main()
	   	