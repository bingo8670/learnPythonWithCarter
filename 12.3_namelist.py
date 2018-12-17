#! python2
print "Enter 5 names:"
names = []
for i in range (1, 6):
    name  = raw_input()
    names.append(name)
print "The third name you entered is:  ", names[2]
