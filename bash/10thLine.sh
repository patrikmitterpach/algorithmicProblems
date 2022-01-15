#!/bin/bash
# Read from the file file.txt and output the tenth line to stdout.

# Head & Tails
cat file.txt | tail +10 | head -1

# AWK
awk 'NR==10 {print $0}' file.txt

# Sed
sed -n "10p" file.txt
