#!/bin/bash

# Ask for the day
read -p 'Challenge Day: ' day

echo Initialising solution and test folder for day $day

# Copy the two directories and rename to contain the day
cp -R ./src/day_xx ./src/day_$day
cp -R ./tests/day_xx ./tests/day_$day

# Then we'll replace xx in the test files with the day number
sed -i '' "s/xx/$day/g" ./tests/day_$day/test_task_01.py
sed -i '' "s/xx/$day/g" ./tests/day_$day/test_task_02.py