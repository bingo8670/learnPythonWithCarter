#! python2
phoneNumbers = {}
phoneNumbers["John"] = "555-1234"
phoneNumbers["Mary"] = "555-6789"
phoneNumbers["Bob"] = "444-4321"
phoneNumbers["Jenny"] = "867-5309"
print phoneNumbers

for value in sorted(phoneNumbers.values()):
    for key in phoneNumbers.keys():
        if phoneNumbers[key] == value:
            #print key, phoneNumbers[key]
            print key, value
