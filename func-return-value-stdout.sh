#!/usr/bin/env bash

function fun1 {
    echo 'return value'
}

function fun2 {
    result=`fun1`
    echo "$result"
}

fun2
