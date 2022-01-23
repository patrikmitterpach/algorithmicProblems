#!/bin/bash

CURRNUM=$1
CURRNUMLEN=$(( $(echo $CURRNUM | wc -c) - 1 ))

printf "Value is "
for (( i=$CURRNUMLEN; i < 5; i++ )); do
    printf "%d" 0
done
printf "%d\n" $CURRNUM

# alternative:
# printf "Value is %05d\n" $CURRNUM