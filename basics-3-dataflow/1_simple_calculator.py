print " [CTRL] + [D] to Terminate"
try:
    while(True):
        print "RESULT \t\t: %.2f" % input("Expression \t: ")

except Exception as e:
    print e
    print "Thank you for using simple_calculator.py!"
