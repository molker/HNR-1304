# HNR-1304 :ballot_box_with_check:
>Mathematics of Democracy examines quantitative aspects of democracy, including methods of voting, apportionment, and redistricting/gerrymandering.
## Research Project :notebook: 
### instantRV.py
* Instant-runoff voting (IRV) is a type of ranked preferential voting method used in single-seat elections with more than two candidates. Instead of indicating support for only one candidate, voters in IRV elections can rank the candidates in order of preference.
* This program was made to work with a research project for the class so the input text files will look different in order to use formatting provided by real world data examples. The dataParse.cpp program is used to format those correctly and will be further described in it's section of the README.
	```bash
	10 A
	2 AB
	6 AC
	13 B
	11 BA
	...
	```
* If you've input everything correctly, your output should look something like this (formatting will change in later iterations):
	```bash
	B Wins 
	```
### dataParse.cpp
* This program was made to take in real world data specifically for the research project involving IRV elections. It is meant to take out all duplicate data becuase there are times where someone will vote for "AAA" which is equivalent to an "A" vote
* The output of this program is formatted the same way, just with more condensed and easier to use data. 
## Other Programs
### bordaCount.py
* The Borda Count method applies weights to votes presented on a preference schedule. The program has been modified to allow any sized preference schedule with any amount of candidates. 
* To use effectively, the parameters should be input in this order (I'd recommend using an input file and using I/O Redirection):
	1. Number of Rows in the Preference Table
	2. Number of Votes from left to right of the table separated by a comma (no spaces)
	3. Each Row (i.e. "ABCD")
* If you've input everything correctly, your output should look something like this (output will vary from case to case depending on number of candidates):
	```bash
	A: 209
	B: 247
	C: 163
	B Wins with 247 points
	```
### pairwise.py
* The Pairwise Comparison method invovles putting every candidate in a head-to-head matchup to see who is able to win the most head-to-head matches. That candidate becomes the winner. 
* To use effectively, the parameters should be input in this order (I'd recommend using an input file and using I/O Redirection):
	1. Number of Rows in the Preference Table
	2. Number of Votes from left to right of the table separated by a comma (no spaces)
	3. Each Row (i.e. "ABCD")
* If you've input everything correctly, your output should look something like this (output will vary from case to case depending on number of candidates):
	```bash
	A Wins with 2 points
	```