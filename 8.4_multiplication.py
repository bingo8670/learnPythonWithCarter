 #! python2
print "Which multiplication table would you like?"
mul = int(raw_input())
print mul
print "How high do you want to go?"
num = int(raw_input())
print "Here's your table:"
i = 1
while i <= num:
   print mul, "*", i, "=", mul * i
   i += 1
