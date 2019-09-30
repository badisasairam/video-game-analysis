#!/usr/bin/python

# Format of each line is:
#Rank,Name,Platform,Year,Genre,Publisher,NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales
#
# We need to write them out to standard output, separated by a tab
# importing the required module which helps us to read the data from the standard input
import sys
# we are reading the file line by line and spliting line based on the comma
for line in sys.stdin:
    data = line.strip().split(",")
    #checking whether the length of the data is 11 becuase we have 11 features in our data
    if len(data) == 11:
        Rank,Name,Platform,Year,Genre,Publisher,NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales = data

        # We need to write them out to standard output, separated by a tab
        print "{0}\t{1}".format(Publisher,NA_Sales)

