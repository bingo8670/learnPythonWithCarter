#! python2
print "Which multiplication table would you like?"
mul = int(raw_input())
print mul
print "Here's your table:"
i = 1
while i <= 10:
    print mul, "*", i, "=", mul * i
    i += 1
