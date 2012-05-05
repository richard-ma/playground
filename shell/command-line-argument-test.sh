#!/usr/bin/env bash

# Usage
# command-line-argument-test.sh (ouput default value)
# Or
# command-line-argument-test.sh hello (output hello)

# exit when error occured
# set -o errexit
# or
set -e
#############################

echo "---------- if ----------"
if [ -n "$1" ]; then
    arg1=$1
else
    arg1="IF DEFAULT VALUE"
fi
echo $arg1

echo "---------- [ -z ] ----------"
arg2=$1
[ -z "$1" ] && arg2="[ -z ] DEFAULT VALUE"
echo $arg2

echo "---------- test -z ----------"
arg3=$1
test -z "$1" && arg3="test -z DEFAULT VALUE"
echo $arg3

echo "---------- [[ -z ]] ----------"
arg4=$1
[[ -z "$1" ]] && arg4="[[ -z ]] DEFAULT VALUE"
echo $arg4

# exit will return last command return value
exit
