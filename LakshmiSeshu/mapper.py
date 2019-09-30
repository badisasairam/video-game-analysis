#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

#It is importing mudule sys
import sys
#Reading the file line by line
for line in sys.stdin:
#It id dividing the line with delimiter as , and storing them in the form of a list
    data = line.strip().split(",")
    if len(data) == 11:
	Rank,Name,Platform,Year,Genre,Publisher,NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales = data
#Printing the results with standard output
        print "{0}\t{1}".format(Platform,Global_Sales)

