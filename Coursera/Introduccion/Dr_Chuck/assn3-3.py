score=raw_input("Enter score between 0.0-1.0: ")

try:
	nscore=float(score)*10
except:
	print "Error, enter a numeric value"
	quit()

if nscore>10:
	print "Error, out of range"

elif nscore<0:
	print "Error, out of range"
else:
	if nscore>=9:
		print "Grade A"
	elif nscore>=8:
		print "Grade B"
	elif nscore>=7:
		print "Grade C"
	elif nscore>=6:
		print "Grade D"
	elif nscore<=6:
		print "Grade F"
