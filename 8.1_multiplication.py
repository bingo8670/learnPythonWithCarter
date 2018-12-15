#! python2
print "Which multiplication table would you like?"
mul = int(raw_input())
print mul
print "Here's your table:"
for i in range (1, 11):
    print mul, "*", i, "=", mul * i
