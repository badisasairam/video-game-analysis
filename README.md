# video-game-analysis
This is our big data project. Our course number is 44517 and group number is 02. <br>

# List of developers
  1. Saikumar Nalivela
  2. Karun Bourishetty
  3. Lakshmi Seshu Kalvakuri
  4. Sairam Badisa
  5. Mallikarjuna Bodepudi
  
# Links
  https://github.com/badisasairam/video-game-analysis <br>
  https://github.com/badisasairam/video-game-analysis/issues
  
# Introduction
  This dataset is going to analyze the sales data from more than 16,500 games. It contains the fields like Rank, Name, Platform, YEAR       etc., and by processing this data we can find the global sales that are done for each year.
  
# DataSource
  This data source contains the data related to the video game analysis which consists of year, Rank, Name etc.  This data consists of       nearly 16,000 records, this is a CSV file. This is a structured data.

# Link to the DataSource
  https://www.kaggle.com/garfieldliang/video-games-analysis
  
# The Challenge
  What makes it a big data challenge?
  •	Volume – Since it has more than 16,000 records to be processed and obtain the required results. <br>
  •	Variety – It has a lot of variety data such as the integer, floating and the object type data. <br>
  •	Veracity – The quality and the accuracy of the data is good since it doesn’t have any null values or the zero values. <br>
  •	Velocity – This Data has no velocity since it is in the past. <br>
  •	Value – using this data source we can calculate the sales and the year in which we got the highest sales according to the genre and               the sport. <br>
  
# Big Data question
  For every year, we can find out the no.of Global Sales for every year in a sorted order. (Sairam Badisa) <br>
  For every year find out the name and the rank of each Video Game in a sorted order. ( Saikumar Nalivela) <br>
  For every year, find out the Genre and the publisher who secured more EU_Sales ( Mallikarjuna Bodepudi) <br>
  For every year, find out the Platform and the genre with NA_Sales ( Karun Bourishetty) <br>
  For every year, find out the Genre and the publisher in a sorted order ( lakshmi Seshu Kalvakuri) <br>
 
# Big Data Solutions
  Sairam Badisa <br>
  •	Mapper Input : One line of data that mapper will read is: <br>
  1 Wii Sports Wii 2006.0 Sports Nintendo 41.49 29.02 3.77 8.46 82.74 <br>
  •	Mapper output/Reducer input : example of an intermediate key-value pair by mapper: <br>
     o	2006.0, 82.74 <br>
     o	1985.0, 40.24 <br>
     o	2008.0, 35.82 <br>
     o	2009.0, 33.00 <br>
     o	1996.0, 31.37 <br>

  •	Reducer output : <br>
  •	Language used: <br>
    The language we are using is python. <br>
  •	What kind of chart will you use to display the results? <br>
    I will use bar chart to display my results. <br>

        
   
        
    
      

      

  
  

