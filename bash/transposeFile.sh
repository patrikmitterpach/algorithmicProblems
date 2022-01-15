#!/bin/bash
# Read from the file file.txt and print its transposed content to stdout.

cat file.txt | cut -d" " -f1,1 | tr "\n" " " >> tmp.txt
echo ""                                      >> tmp.txt
cat file.txt | cut -d" " -f2,2 | tr "\n" " " >> tmp.txt
echo ""                                      >> tmp.txt

cat tmp.txt; rm tmp.txt
