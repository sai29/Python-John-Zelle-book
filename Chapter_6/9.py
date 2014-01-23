# A certain CS professor gives 5-point quizzes that are graded on the scale
# 5-A, 4-B, 3-C, 2-D, 1-F, 0-F. Write a program that accepts a quiz score as an
# input and prints out the corresponding grade.

def main():
	mark = int(raw_input("Enter the mark: "))
	mark1 = grader(mark)

def grader(mark):
	grades = ["F","E","D","C","B","A"]
	markstr = grades[mark]
	print  "The mark is %s" %(markstr)

main()

