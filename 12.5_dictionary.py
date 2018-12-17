#! python2
aOrl = raw_input("Add or look up a word (a/l)?"  )
dictionary = { }
#word       = raw_input("Type the word:  ")
#definition = raw_input("Type the definition:  ")
#dictionary[word] = definition
#print "Word added!"
while aOrl in ['a', 'l']:
    if aOrl == "a":
        word       = raw_input("Type the word:  ")
        definition = raw_input("Type the definition:  ")
        dictionary[word] = definition
        print "Word added!"
    elif aOrl == "l":
        word       = raw_input("Type the word:  ")
        if word in dictionary:
            print dictionary[word]
        else:
            print "That word isn't in the dictionary yet."
    aOrl = raw_input("Add or look up a word (a/l)?"  )
