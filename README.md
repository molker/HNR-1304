# HNR-1304 :ballot_box_with_check:
>Mathematics of Democracy examines quantitative aspects of democracy, including methods of voting, apportionment, and redistricting/gerrymandering.
1. BordaCount.py
	* The Borda Count method applies weights to votes presented on a preference schedule. The program has been modified to allow any sized preference schedule with any amount of candidates. 
	* To use effectively, the parameters should be input in this order (I'd recommend using an input file and using I/O Redirection):
		1. Number of Candidates 
		2. Number of Rows in the Preference Table
		3. Number of Votes from left to right of the table separated by a comma (no spaces)
		4+. Each Row (i.e. "ABCD")
	* If you've input everything correctly, your output should look something like this (output will vary from case to case depending on number of candidates):
		```bash
		A: 209
		B: 247
		C: 163
		```
