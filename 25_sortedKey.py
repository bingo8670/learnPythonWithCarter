#! python2
phoneNumbers = {}
phoneNumbers["John"] = "555-1234"
phoneNumbers["Mary"] = "555-6789"
phoneNumbers["Bob"] = "444-4321"
phoneNumbers["Jenny"] = "867-5309"
print phoneNumbers

for key in sorted(phoneNumbers.keys()):
    print key, phoneNumbers[key]
