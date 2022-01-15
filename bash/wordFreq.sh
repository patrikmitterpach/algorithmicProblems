#!/bin/bash

# 192. Word Frequency
# Write a bash script to calculate the frequency of each word in a text file words.txt.
# For simplicity sake, you may assume:
#	words.txt contains only lowercase characters and space ' ' characters.
#	Each word must consist of lowercase characters only.
#	Words are separated by one or more whitespace characters.

cat words.txt | tr -s " " "\n" | sort | uniq -c  | tr -s " " | sort -nr | awk '{print $2, $1}'
