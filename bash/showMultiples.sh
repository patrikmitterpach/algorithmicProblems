#!/bin/bash

# Print all numbers up to 3rd parameter
#  which are multiple of both 1st and 2nd parameter.

for (( i=1; i <= $3; i++ )); do
    if [ $(( $i % $2 ))  == 0 ] && [ $(( $i % $1 )) == 0 ] ; then
        echo "$i"
    fi
done