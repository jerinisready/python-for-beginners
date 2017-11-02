
import sys
print ""
 
args = sys.argv
try:
	print(args)
	print("")
	a = int(args[1])
	b = int(args[3])

	if args[2] == '+':
		print "\tRESULT : ",a + b

	elif args[2] == '-':
		print "\tRESULT : ",a - b

	elif args[2] == 'x':
		print "\tRESULT : ",a * b

	elif args[2] == '/':
		print "\tRESULT : ",a / b

	elif args[2] == '%':
		print "\tRESULT : ",a % b

	else:	raise Exception
	
except Exception as e:
	print "Usage 'python simple_calculator.py <num1> < +-x/% > <num2>    "
	print"Some Error Occured : %s" % e
print ""
print "Thank you for using simple_calculator.py!"

