import math

def main():
	inch = float(raw_input("Enter the inches"))
	prices = float(raw_input("Enter the price"))
	area1 = area(inch)
	price1 = price(area1,prices)
	print "The area is ", area1
	print "The price per square inch is", price1

def area(inches):
	tarea = ( 3.14 * inches * inches)
	return tarea

def price(area1,prices):
	tprice = area1 / prices
	return tprice

main()