#!/bin/bash

echo $1 | sed 's/./&\n/g'      \
        | nl                    \
        | sort -r                \
        | awk '{print $2}'        \
        | tr -d '\n '              \
        | sed 's/^0*//g'

printf "\n" 