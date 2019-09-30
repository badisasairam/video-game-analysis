#!/usr/bin/python

import sys

salesTotal = 0
oldKey = None



#
# All the sales for a particular store will be presented,


# Loop around the data
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
# It will be in the format key\tval

# Where key is the Platform, val is the global sales
    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", salesTotal
        oldKey = thisKey;
        salesTotal = 0

# All the sales for a particular store will be presented,
    oldKey = thisKey
    salesTotal += float(thisSale)
# then the key will change and we'll be dealing with the next store
if oldKey != None:
    print oldKey, "\t", salesTotal

