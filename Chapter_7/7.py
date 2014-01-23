def main():
	shour = float(raw_input("Enter the starting hours "))
	smin = float(raw_input("Enter the starting minutes "))
	ehour = float(raw_input("Enter the ending hours "))
	emin = float(raw_input("Enter the ending minutes: "))
	cperiodh = ehour-shour
	cperiodm = emin -smin
	cperiodm1 = cperiodm / 60                                                               
	fperiod = cperiodh + cperiodm1
	if ehour < 9:
		charge = fperiod * 2.50
		print "Your payable ammount is %f " %(charge)
	if ehour >= 9:
		shour1 = (9-(shour + (smin / 60)))
		ehour1 = ((ehour + (emin / 60)-9))
		fcharge1 = (shour1* 2.50 )+ (ehour1  * 1.75)
		print "Your payable amount is %f" %(fcharge1)
main() 

	
 