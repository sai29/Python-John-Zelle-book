def main():
	slimit = int(raw_input("Enter the speed limit"))
	ospeed = int(raw_input("Enter the clocked speed: "))
	diff = ospeed - slimit
	if ospeed < slimit:
		print "You are driving safely."
	elif ospeed <= 90 and ospeed > slimit:
		print "You are overspeeding."
		fine = 50 + (diff * 5)
		print "Your fine is %d dollars." %(fine)
	elif ospeed > 90 and ospeed > slimit:
		fine = 50 + 200 + (diff*5)
		print "Your fine is %d dollars.0" %(fine)
main() 