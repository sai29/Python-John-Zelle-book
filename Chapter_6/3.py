

def sphereArea(radius):
	area = 4 * 3.14 * (radius * radius) 
	return area

def sphereVolume(radius):
	vol = (4 / 3) * (3.14 * (radius * radius))
	return vol

def main():
	rad = float(raw_input("Enter the value of the radius"))
	area1 = sphereArea(rad)
	volume = sphereVolume(rad)
	print "The area is", area1
	print "The volume is", volume



main()

