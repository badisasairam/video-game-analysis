#!/usr/bin/python

import sys

# total northamerica sales as salestotal
salesTotal = 0
# old key refers to each genre
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    # Here we split each line with "\t" as a delimeter
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", salesTotal
        oldKey = thisKey
        salesTotal = 0

    oldKey = thisKey
    #Here we add the total sales for each key
    salesTotal += float(thisSale)

if oldKey != None:
    print oldKey, "\t", salesTotal

