#!/bin/bash


#Array of Tests
array=( test_add.jsql test_sub.jsql test_addjson12.jsql test_addjson21.jsql )

#Monitor passed and failed tests
passed = 0
failed = 0


for i in "${array[@]}"
do
	#python ../main.py tests/$i > output.txt
	if [[ -n $(diff tests/results/result_$i output.txt) ]]; then
		echo "----- Test "$i" Failed -----"
		diff tests/results/result_$i output.txt
		failed=$((failed+1))
	else
		echo "------Test "$i" Passed -----"	
		passed=$((passed+1))
	fi
done

echo "------------------------"
echo "| # of Tests Passed: "$failed" |"
echo "| # of Tests Failed: "$passed" |"
echo "------------------------"

 