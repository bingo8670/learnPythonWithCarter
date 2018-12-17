#! python2
seconds = int(raw_input('Countdown timer:  How many seconds? ' ))
import time
for i in range (seconds, 0, -1):
    print i, "* " * i
    time.sleep(1)
print "BLAST OFF!"
