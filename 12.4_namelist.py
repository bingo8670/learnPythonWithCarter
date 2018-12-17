#! python2
print "Enter 5 names:"
names = []
for i in range (1, 6):
    name  = raw_input()
    names.append(name)

print "The names are ",
for name in names:
    print name,

print
num = int(raw_input("Replace one name. Which one?  (1-5):"))
print num
new_name = raw_input("New name: ")
print new_name
names[num -1] = new_name

print "The names are ",
for name in names:
    print name,
