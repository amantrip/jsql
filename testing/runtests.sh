#!/bin/bash

array=( tests/test1.jsql tests/test2.jsql )
for i in "${array[@]}"
do
	python ../main.py $i > output.txt
	# Add a comparison script to see if the results matched the output
done


 