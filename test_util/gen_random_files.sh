#!/bin/bash

for ((i=1; i<=$1; ++i))
do
    dd if=/dev/urandom of=./$i.data bs=$2 count=1
done
