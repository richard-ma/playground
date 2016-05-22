#!/bin/bash

for ((i=1; i<=$1; ++i))
do
    dd if=/dev/urandom of=./$i.html bs=$2 count=1
done
