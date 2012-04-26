#!/usr/bin/env bash

parentid=$1
test -z "$1" && parentid=0
myid=`expr $parentid + 1`
echo "I'm ROBOT #$myid. Made by #$parentid"

# invoke myself
./re-invoke.sh $myid
