#!/usr/bin/env bash

function func {
    myid=`expr $1 + 1`
    echo "myid is $myid"
    func $myid
}

func
