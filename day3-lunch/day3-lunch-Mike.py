#!/usr/bin/env python

import random
r = random.randint(1,100)

nums=range(0, 100, 10)
print nums

key = 80
#initializing the whole is to be searched
lo =0 
high=len(nums)
#main loop: keep going while there are options available
while lo<high:
    mididx=(lo+high)/2
    mid = nums[mididx]
 #compare middle item to list   
    if mid==key:
        print "Hooray! Found it at %d" % mididx
        break
    elif key>mid:
        lo=mididx+1
    else:
        high=mididx