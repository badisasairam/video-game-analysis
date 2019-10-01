#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

for line in sys.stdin:
     # This line reads the data and split it with the delimiter ",". <br>
    data = line.strip().split(",")
     # this if condition checks each modules whether it is equal to 11. <br>
    if len(data) == 11:
     # if it is equal then all the fields are going to be assigned to data. <br>
        Rank, Name, Platform, Year, Genre, Publisher, NA_Sales, EU_Sales, JP_Sales, Other_Sales, Gloabal_Sales = data
     # print the values.
        print ("{0}\t{1}".format(Year, Global_Sales))

