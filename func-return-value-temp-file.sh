#!/usr/bin/env bash

return_value_temp_file='return-value'

function fun1 {
    echo 'return value' > "$return_value_temp_file"
}

function fun2 {
    fun1; result=`cat $return_value_temp_file`
    echo "$result"
}

fun2
