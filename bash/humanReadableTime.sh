#!/bin/bash

# Write a function, which takes a non-negative integer (SECONDS) 
#   as input and returns the time in a human-readable format (HH:MM:SS):
#   
#   HH = hours, padded to 2 digits, range: 00 - 99
#   MM = minutes, padded to 2 digits, range: 00 - 59
#   SS = seconds, padded to 2 digits, range: 00 - 59

SECONDS=$1

HOURS=$(( $SECONDS / 3600))
SECONDS=$(($SECONDS % 3600))
MINUTES=$(($SECONDS / 60))
SECONDS=$(($SECONDS % 60))

printf "%02d:%02d:%02d\n" $HOURS $MINUTES $SECONDS