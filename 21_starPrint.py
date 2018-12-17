#! python2
numBlocks = int(raw_input('How many blocks of stars do you want?  '))
numLines = int(raw_input ('How many lines of stars do you want?  '))
numStars = int(raw_input ('How many stars per line?  '))
for block in range(0, numLines):
    for line in range(0, numLines):
        for star in range(0, numStars):
            print "*",
        print
    print
