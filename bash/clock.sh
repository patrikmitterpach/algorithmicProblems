#!/bin/bash
# Clock shows h hours, m minutes and s seconds after midnight.
# Your task is to write a function which returns the time since midnight in milliseconds.

printf "%d\n" $(( $1 * 3600000 + $2 * 60000 + $3 * 1000 ))