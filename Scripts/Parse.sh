#!/bin/bash

for file in `ls ../RAW/`
do
	if [ ! -a "../TestFiles/$file" ]; then
			touch "../TestFiles/$file"
	fi
	../a.out < "../RAW/$file" > "../TestFiles/$file"
done