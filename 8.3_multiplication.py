#! python2
print "Which multiplication table would you like?"
mul = int(raw_input())
print mul
print "How high do you want to go?"
num = int(raw_input())
print "Here's your table:"
for i in range (1, num+1):
   print mul, "*", i, "=", mul * i
