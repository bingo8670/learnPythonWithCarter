#! python2
V = int(raw_input("the size of tank L : "))
P = int(raw_input("percent of full oil : "))
v= int(raw_input("km per liter : "))

S = V * P / 100 * v
print "The next station is 200 km away."

print "You can go another",
print(S),
print "km away."

if S > 200:
    print "You can wait for the next station."
else:
    print "Get gas now!"
