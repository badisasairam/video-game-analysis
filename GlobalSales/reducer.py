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
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone lwrong. Skip this line. <br>
        continue
        # this step assigns the values of the data_mapped to the thisKey, thisSale. <br>
    thisKey, thisSale = data_mapped
    
        # if oldKey and oldkey not equals to thisKey then it is going to print both values and assign thisKey to oldKey and salesTotal to 0. <br>
    if oldKey and oldKey != thisKey:
        print oldKey, "\t", salesTotal
        oldKey = thisKey
        salesTotal = 0

        # this steps proceeds with the assigning the thisKey to oldKey and float value of thisSale to salesTotal. <br>
    oldKey = thisKey
    salesTotal += float(thisSale)
        # if oldKey is not equal to anything then it is going to print oldKey and salesTotal. <br>
if oldKey != None:
    print oldKey, "\t", salesTotal

