#! python2
sex = str(raw_input("what's your sex, m or f ?"))
if sex == "m":
    print "Sorry, you are't suitable for team."
else:
    age = int(raw_input("How old are you ?"))
    if 10 <= age <= 12:
        print "Congratulations, you can join the football team."
    else:
        print "Sorry, you are't suitable for team."


