


import string

def main():
	n = int(raw_input("Enter the number of inputs"))
	output = ""
	for acronym in range(n):
		acronym = raw_input("Enter the input: ")
		acronym1 = string.capwords(acronym)
		
		list(acronym1)
		
	print output

main()
