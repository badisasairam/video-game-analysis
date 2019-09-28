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
  This dataset gives the sales count of video games in north america, europe and japan. It contains the fields like Rank, Name, Platform, YEAR       etc., and by processing this data we can find the global sales that are done for each year.
  
# DataSource
  This data source contains the data related to the video game analysis which consists of year, Rank, Name etc.  This data consists of       nearly 16,000 records, this is a CSV file. This is a structured data.

# Link to the DataSource
  https://www.kaggle.com/garfieldliang/video-games-analysis
  
# The Challenge
  What makes it a big data challenge? <br>
  &emsp; •	Volume – Since it has more than 16,000 records to be processed and obtain the required results. <br>
  &emsp; •	Variety – It has a lot of variety data such as the integer, floating and the object type data. <br>
  &emsp; •	Veracity – The quality and the accuracy of the data is good since it doesn’t have any null values or the zero values. <br>
  &emsp; •	Velocity – This Data has no velocity since it is in the past. <br>
  &emsp; •	Value – using this data source we can calculate the sales and the year in which we got the highest sales according to the               genre and the sport. <br>
  
# Big Data question
  For every year, we can find out the no.of Global Sales for every year in a sorted order. (Sairam Badisa) <br>
  For the platform ps4,  find the highest saled game under the publisher "Sony Computer Entertainment". ( Saikumar Nalivela) <br>
  For every year, find out the Genre and the publisher who secured more EU_Sales ( Mallikarjuna Bodepudi) <br>
  For every year, find out the Platform and the genre with NA_Sales ( Karun Bourishetty) <br>
  For any publisher, find the highest rank game developed in north america? ( lakshmi Seshu Kalvakuri) <br>
 
# Big Data Solutions
  Sairam Badisa <br>
  &emsp;•	Mapper Input : One line of data that mapper will read is: <br>
  &emsp; &emsp;1 Wii Sports Wii 2006.0 Sports Nintendo 41.49 29.02 3.77 8.46 82.74 <br>
  &emsp;•	Mapper output/Reducer input : example of an intermediate key-value pair by mapper: <br>
  &emsp;&emsp;   o	2006.0, 82.74 <br>
  &emsp;&emsp;   o	1985.0, 40.24 <br>
  &emsp;&emsp;   o	2008.0, 35.82 <br>
  &emsp;&emsp;   o	2009.0, 33.00 <br>
  &emsp;&emsp;   o	1996.0, 31.37 <br>
  &emsp;•	Reducer output : <br>
  &emsp;&emsp;   o	1985.0, 40.24 <br>
  
  &emsp;•	Language used: <br>
  &emsp;&emsp;  The language we are using is python. <br>
  &emsp;•	What kind of chart will you use to display the results? <br>
  &emsp;&emsp;  I will use bar chart to display my results. <br>
    
   Lakshmi Seshu Kalvakuri <br>
&emsp; •	Mapper Input : One line of data that mapper will read is: <br>
&emsp; &emsp; 2598	Alien	2600	1981	Action	20th Century Fox Video Games	0.74	0.04	0	0.01	0.79<br>
&emsp; •	Mapper output/Reducer input : example of an intermediate key-value pair by mapper: <br>
&emsp; &emsp;  Rank	Name	Year	Publisher	NA_Sales<br>
&emsp; &emsp; 2598	Alien	1981	20th Century Fox Video Games	0.74<br>
&emsp; &emsp; 5391	Fantastic Voyage	1981	20th Century Fox Video Games	0.32<br>
&emsp; &emsp; 5397	Bank Heist	1982	20th Century Fox Video Games	0.32<br>
&emsp; &emsp; 6730	Porky's	1982	20th Century Fox Video Games	0.23<br>
&emsp; &emsp; 7150	Deadly Duck	1981	20th Century Fox Video Games	0.21<br>
&emsp; •	Reducer output : <br>
&emsp;&emsp; Rank	Name	Year	Publisher	NA_Sales<br>
&emsp; &emsp;2598	Alien	1981	20th Century Fox Video Games	0.74<br>
&emsp; •	Language used: <br>
&emsp;&emsp; The language we are using is python. <br>
&emsp; •	What kind of chart will you use to display the results? <br>
&emsp;&emsp; I will use bar chart to display my results. <br>

Saikumar Nalivela <br>
&emsp; •	Mapper Input : One line of data that mapper will read is: <br>
&emsp; &emsp;237	The Last of Us	PS4	2014	Action	Sony Computer Entertainment
&emsp; •	Mapper output/Reducer input : example of an intermediate key-value pair by mapper: <br>
&emsp; &emsp;Rank	Name	Platform	Year	Genre	Publisher <br>
&emsp; &emsp;237	The Last of Us	PS4	2014	Action	Sony Computer Entertainment <br>
&emsp; &emsp;244	Uncharted: The Nathan Drake Collection	PS4	2015	Action	Sony Computer Entertainment <br>
&emsp; &emsp;272	Uncharted 4: A Thief's End	PS4	2016	Shooter	Sony Computer Entertainment <br>
&emsp; &emsp;539	inFAMOUS: Second Son	PS4	2014	Action	Sony Computer Entertainment <br>
&emsp; &emsp;594	Killzone: Shadow Fall	PS4	2013	Shooter	Sony Computer Entertainment <br>
&emsp; &emsp;662	Bloodborne	PS4	2015	Action	Sony Computer Entertainment <br>
&emsp; &emsp;850	DriveClub	PS4	2014	Racing	Sony Computer Entertainment <br>
&emsp; &emsp;931	LittleBigPlanet 3	PS4	2014	Platform	Sony Computer Entertainment <br>
&emsp; •	Reducer output : <br>
&emsp; &emsp;Rank	Name	Platform	Genre	Publisher
&emsp; &emsp;237	The Last of Us	PS4	Action	Sony Computer Entertainment <br>
&emsp; &emsp;244	Uncharted: The Nathan Drake Collection	PS4	Action	Sony Computer Entertainment <br>
&emsp; &emsp;272	Uncharted 4: A Thief's End	PS4	Shooter	Sony Computer Entertainment <br>
&emsp; &emsp;539	inFAMOUS: Second Son	PS4	Action	Sony Computer Entertainment <br>
&emsp; &emsp;594	Killzone: Shadow Fall	PS4	Shooter	Sony Computer Entertainment <br>
&emsp; &emsp;662	Bloodborne	PS4	Action	Sony Computer Entertainment <br>

&emsp; •	Language used: <br>
&emsp;&emsp; The language we are using is python. <br>
&emsp; •	What kind of chart will you use to display the results? <br>
&emsp;&emsp; I will use bar chart to display my results. <br>


Karun Bourishetty<br>
&emsp; •	Mapper Input : One line of data that mapper will read is: <br>
&emsp; &emsp;259	Asteroids	2600	1980	Shooter	Atari	4	0.26	0	0.05	4.31 <br>
&emsp; •	Mapper output/Reducer input : example of an intermediate key-value pair by mapper: <br>
&emsp; &emsp;Rank	Name	Platform	Year	Genre	Publisher	NA_Sales	EU_Sales	JP_Sales	Other_Sales	Global_Sales <br>
&emsp; &emsp;259	Asteroids	2600	1980	Shooter	Atari	4	0.26	0	0.05	4.31 <br>
&emsp; &emsp;545	Missile Command	2600	1980	Shooter	Atari	2.56	0.17	0	0.03	2.76 <br>
&emsp; &emsp;1768	Kaboom!	2600	1980	Misc	Activision	1.07	0.07	0	0.01	1.15 <br>
&emsp; &emsp;1971	Defender	2600	1980	Misc	Atari	0.99	0.05	0	0.01	1.05 <br>
&emsp; &emsp;2671	Boxing	2600	1980	Fighting	Activision	0.72	0.04	0	0.01	0.77 <br>
&emsp; &emsp;4027	Ice Hockey	2600	1980	Sports	Activision	0.46	0.03	0	0.01	0.49 <br>
&emsp; &emsp;5368	Freeway	2600	1980	Action	Activision	0.32	0.02	0	0	0.34 <br>
&emsp; &emsp;6319	Bridge	2600	1980	Misc	Activision	0.25	0.02	0	0	0.27 <br>
&emsp; &emsp;6898	Checkers	2600	1980	Misc	Atari	0.22	0.01	0	0	0.24 <br>
&emsp; •	Reducer output : <br>
&emsp; &emsp;Rank	Name	Platform	Genre	Publisher <br>
&emsp; &emsp;Rank	Name	Platform	Year	Genre	Publisher <br>
&emsp; &emsp;259	Asteroids	2600	1980	Shooter	Atari <br>
&emsp; &emsp;545	Missile Command	2600	1980	Shooter	Atari <br>
&emsp; &emsp;1768	Kaboom!	2600	1980	Misc	Activision <br>
&emsp; &emsp;1971	Defender	2600	1980	Misc	Atari <br>
&emsp; &emsp;2671	Boxing	2600	1980	Fighting	Activision <br>
&emsp; &emsp;4027	Ice Hockey	2600	1980	Sports	Activision <br>
&emsp; &emsp;5368	Freeway	2600	1980	Action	Activision <br>
&emsp; &emsp;6319	Bridge	2600	1980	Misc	Activision <br>
&emsp; &emsp;6898	Checkers	2600	1980	Misc	Atari <br>


&emsp; •	Language used: <br>
&emsp;&emsp; The language we are using is python. <br>
&emsp; •	What kind of chart will you use to display the results? <br>
&emsp;&emsp; I will use bar chart to display my results. <br>

Mallikaarjun Bodepudi<br>
&emsp; •	Mapper Input : One line of data that mapper will read is: <br>
&emsp; &emsp; 1	Wii Sports	Wii	2006	Sports	Nintendo	41.49	29.02	3.77	8.46	82.74
&emsp; •	Mapper output/Reducer input : example of an intermediate key-value pair by mapper: <br>
&emsp; &emsp;1	Wii Sports	Wii	2006	Sports	Nintendo	41.49	29.02 <br>
&emsp; &emsp;2	Super Mario Bros.	NES	1985	Platform	Nintendo	29.08	3.58<br>
&emsp; &emsp;3	Mario Kart Wii	Wii	2008	Racing	Nintendo	15.85	12.88 <br>
&emsp; &emsp;&emsp; &emsp;4	Wii Sports Resort	Wii	2009	Sports	Nintendo	15.75	11.01 <br>
&emsp; &emsp;5	Pokemon Red/Pokemon Blue	GB	1996	Role-Playing	Nintendo	11.27	8.89 <br>
&emsp; &emsp;6	Tetris	GB	1989	Puzzle	Nintendo	23.2	2.26 <br>
&emsp; &emsp;7	New Super Mario Bros.	DS	2006	Platform	Nintendo	11.38	9.23 <br>
&emsp; &emsp;8	Wii Play	Wii	2006	Misc	Nintendo	14.03	9.2 <br>
&emsp; &emsp;9	New Super Mario Bros. Wii	Wii	2009	Platform	Nintendo	14.59	7.06 <br>
&emsp; &emsp;10	Duck Hunt	NES	1984	Shooter	Nintendo	26.93	0.63 <br>
&emsp; •	Reducer output : <br>
&emsp; &emsp;1	Wii Sports	Wii	2006	Sports	Nintendo<br>
&emsp; &emsp;2	Super Mario Bros.	NES	1985	Platform	Nintendo <br>
&emsp; &emsp;3	Mario Kart Wii	Wii	2008	Racing	Nintend0 <br>
&emsp; •	Language used: <br>
&emsp;&emsp; The language we are using is python. <br>
&emsp; •	What kind of chart will you use to display the results? <br>
&emsp;&emsp; I will use bar chart to display my results. <br>


        
    
      

      

  
  

