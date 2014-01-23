# As discussed in the chapter, string formatting could be used to simplify the
# dateconver2.py program. Go back and redo this program making use
# of the string-formatting operator.


import string

def main():
    day, month, year = input("Please enter the day, month and year numbers: ")

    date1 = str(month)+"/"+str(day)+"/"+str(year)

    months = ["January", "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November", "December"]
    monthStr = months[month-1]
    

    
    print "The date is %s,the month is %s,the year is %s" %(day,monthStr,year) 

main()



