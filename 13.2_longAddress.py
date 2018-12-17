#! python2
# define a function with seven arguments
def printAddr(name, num, street, city, prov, pcode, country):
    print name
    print num,
    print street
    print city,
    if prov !="":
        print ", "+prov
    else:
        print ""
    print pcode
    print country
    print

#call the function and pass seven arguments to it
printAddr("Sam","45", "Main St.","Ottawa", "ON", "K2M 2E9","Canada")
#printAddr("Jian," "64", "2nd Ave.","Hong Kong", " ", "235643","China")
