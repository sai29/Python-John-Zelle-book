hydracarbon#This program calculate the molecular weight of the hydrocarbon based 
#on the number of hydrogen,carbon,oxygen atoms given the weights as
#       Atom            Weight(grams/mole)

#       H                       1.0079
#       c                       12.011
#       o                       15.9994

def main():

        print "\n\n\n"

        H = input ("Enter the number of 'hydrogen' atoms in the hydrocarbon : ")

        C = input ("Enter the number of 'carbon' atoms in the hydrocarbon : ")

        O = input ("Enter the number of 'oxygen' atoms in the hydrocarbon : ")

#This prints the values we used for the weights of the atoms
#       print "\nWeight(gram/mole) of hydrogen atom = 1.0079"
#       print "Weight(gram/mole) of carbon atom = 12.011"
#       print "Weight(gram/mole) of oxygen atom = 15.9994\n"

#       print "The number of hydrogen atoms entered is ",H,""
#       print "The number of carbon atoms entered is ",C,""
#       print "The number of oxygen atoms entered is ",O,"\n"

        HW = 1.0079
        CW = 12.011
        OW = 15.9994

        MW = float (float(H * HW) + float(O* OW) + float(C * CW))  #calculation of the molecular weight of the hydrocarbon in gram/mole
        print "The molecular weight of the hydrocarbon in (gram/mole) is ",MW, "\n\n\n"


