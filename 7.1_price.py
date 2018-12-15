#! python2
#-*- coding: UTF-8 -*-
price = float(raw_input("What's the price of it?"))
if price <= 10:
    total = 0.9 * price
    print "您的折扣是10%"
else:
    total = 0.8 * price
    print "您的折扣是20%"

print "您的最终价格是"
print total
