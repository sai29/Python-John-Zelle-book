import math

def main():
    s1 = float(raw_input("Enter the sides: "))
    s2 = float(raw_input("Enter the sides: "))
    s3 = float(raw_input("Enter the sides: "))
    area1 = area(s1,s2,s3)
    print "The area is", area1

def area(p1,p2,p3):
    s = (p1+p2+p3)/ 2
    print s
    a = math.sqrt(float(s*(s-p1)*(s-p2)*(s-p3)))
    return a

main()