def main():
	no1 = int(raw_input("Enter the number: "))
	print no1
	while no1 >= 1:
		if no1 % 2 != 0:
			no1 = 3 * no1 + 1
			print no1
		elif no1 % 2 == 0:
				no1 = no1 / 2
				print no1

		if no1 == 1:break
main()
