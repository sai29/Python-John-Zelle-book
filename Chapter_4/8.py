import string
def main():
    print "This program converts a textual message into a sequence"
    print "of numbers representing the ASCII encoding of the message."
    print
    
    # Get the message to encode
    message = raw_input("Please enter the message to encode: ")
    n = int(raw_input("Enter the key value"))
    print
    print "Here are the ASCII codes:"
    
    # Loop through the message and print out the ASCII values
    for ch in message:
        a = chr(ord(ch) + n),   # use comma to print all on one line.
        print " ".join(a),
    print

main()
