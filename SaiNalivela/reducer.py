#!/usr/bin/python

import sys

salesTotal = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    # we are reading the file line by line and spliting line based on the "tab space"
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
        #assigning the list vaues to thisKey and thisSale 
    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", salesTotal
        oldKey = thisKey;
        salesTotal = 0

    oldKey = thisKey
    # Adding all the similar items sales together to find the aggreagte sales of the publisher
    salesTotal += float(thisSale)

if oldKey != None:
    print oldKey, "\t", salesTotal

