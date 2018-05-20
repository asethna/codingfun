###########################################
################# PARSER ##################
###########################################
How to calculate statistics of streaming rate:
1. Open Command Prompt
2. In command line call: >>python.exe parser.py <streaming_rate_log_file.txt>
3. The program will run finding the rates and calculates:
	Average - Calculates the average rate of given input file.
	Minimum - Find the minimum rate from given input file and the time it occured.
	Maximum - Find the maximum rate from given input file and the time it occured.
	Middle - Sorting the rates, find the middle value and the time it occured.
Note: All rates should be defined as "Old=22.686(MBps) New=20.032(MBps)".
Date should be in following format: "YYYY-MM-DDTHH:mm:SS.fffZ"
	where YYYY is year, MM is month, DD is day
	where HH is hour, mm is minute, SS is seconds, fff is microsecond.
Speeds measurements are disregarded (i.e. MBps).

Testing:
Currently supported for Windows 10 using Python version 2.7.15.
Testing with different size of rate files with different values and inputs
to determine that the script holds.