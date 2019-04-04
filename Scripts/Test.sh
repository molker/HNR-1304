#!/bin/bash
# Test.sh
# Name: Matthew Olker
# Date: 3-8-2019
# Class: HNR-1304

#Test Answers function
#Parameters:
#	0: Test.sh
#	1: Program file name
#	2: Replace or Append
testAnswers()
{
	# If the Directory TestFiles doesn't exist then exit script
	if [ ! -d "../TestFiles/" ]; then
		echo "Test.sh: TestFiles directory doesn't exist or isn't in the right place"
		exit 1
	fi
	
	# If the Directory OutFiles doesn't exist then create the Directory
	if [ ! -d "../OutFiles/" ]; then
		mkdir "../OutFiles/"
		echo "Test.sh: OutFiles directory made"
	fi
	
	# for each file in TestFiles test if it is a link / directory
	# if neither then create a file in OutFiles to hold output data and run code
	for file in `ls ../TestFiles/`
	do
		if test -L $file
		then
			echo "Test.sh: $file is a link"
		elif [[ -d $file ]]; then
			echo "Test.sh: $file is a directory"
		else
			if [ ! -a "../OutFiles/$file" ]; then
				touch "../OutFiles/$file"
			fi
			# if another voting method in the same run has already been print out
			# append to the file instead of replacing current information
			if [ "$2" = append ]; then
				echo " " >> "../OutFiles/$file"
				echo "$1" >> "../OutFiles/$file"
				python $1 < "../TestFiles/$file" >> "../OutFiles/$file"
			else
				echo $file
				echo "$1" > "../OutFiles/$file"
				python $1 < "../TestFiles/$file" >> "../OutFiles/$file"
			fi
		fi

	done
}

#Parameters: 
#	0: Test.sh
#	1: Voting Method
if [ ! -x $2 ]; then
	echo "Test.sh: Executable does not exist"
	exit 3
fi

# depending on the 1st argument run the code through testAnswers and then run it
chosen=true
case "$1" in 
	pairwise)
		testAnswers pairwise.py 
		;;
	borda) 
		testAnswers bordaCount.py 
		;;
	irv)
		testAnswers instantRV.py
		;;
	all) 
		testAnswers pairwise.py 
		testAnswers bordaCount.py append
		;;
	*) 
		echo "Test.sh: Make sure you wrote the voting method name correctly!"
		chosen=false
		;;
esac

# Change this to be only if it doesn't run the "make sure you wrote the voting method correctly"
if [ "$chosen" = true ] ; then
	echo "Testing $1 Successful"
fi 