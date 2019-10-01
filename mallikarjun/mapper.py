#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

# We are reading each line from standarinput
for line in sys.stdin:
    # Here we split each line with "," as a delimeter
    data = line.strip().split(",")
    # Here we check the length of the data equal to 11. ignoring all the lines which are lessthan and greaterthan 11
    if len(data) == 11:
	    Rank,Name,Platform,Year,Genre,Publisher,NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales = data
        # selecting only Genre for Northamerica sales
        print ("{0}\t{1}".format(Year,EU_Sales))

