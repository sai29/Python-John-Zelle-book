def main():
	weight = float(raw_input("Enter the weight: "))
	height = float(raw_input("Enter the height: "))
	weight1 = weight * 720
	height1 = height * height
	bmi = weight1 / height1
	print "Your bmi is %f" %(bmi)
	if bmi > 18 and bmi <= 25:
		print "You are healthy"

	if bmi < 19:
		print "You are under-weight"

	if bmi > 25:
		print "You are over-weight"
main()

