#!/bin/bash

# Count the number of Duplicates
#   Write a function that will return the count of distinct case-insensitive
#   alphabetic characters and numeric digits that occur more than once in the input string.
#   The input string can be assumed to contain only alphabets 
#   (both uppercase and lowercase) and numeric digits.

echo $1 | tr "[:upper:]" "[:lower:]" \
        | sed 's/./&\n/g'             \
        | sort                         \
        | uniq -c                       \
        | awk -v SUM=0 '$1 > 1 {SUM = SUM+1}; END {print SUM}'