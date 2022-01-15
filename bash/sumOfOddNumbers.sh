n=$1

## 1. Actually draws the pyramid, runtime too long, roughly O(n**2)
## 	ODD_COUNT=1
## 	rm pyramid.txt
## 
## 	for (( i = 1; i <= $n; i++ )) do
## 		for ((j = 0; j < $i; j++ )) do
## 			printf "%d " $ODD_COUNT >> pyramid.txt
## 			ODD_COUNT=$(( $ODD_COUNT + 2))
## 	done
## 	printf "\n" >> pyramid.txt
##	done
##
## 	cat pyramid.txt | tail -1 | tr ' ' '\n' | awk '{sum += $0} END {print sum}'
## 	rm pyramid.txt
## 
## 
## # 2. Easier mathematical edition O(n)
## 
## # Denotes the first number on the line
## LINE_START=$(( $n**2 - $n + 1))
## 
## echo $(($LINE_START ))
## for (( i = 0; i < $n; i++ )); do
## 	SUM=$(( $SUM + $LINE_START ))
## 	LINE_START=$((LINE_START + 2))
## 	echo $SUM
## done
## 
## echo $SUM


# 3. Math Overload O(1)
LINE_START=$(( $n**2 - $n + 1))
echo $(($n * $LINE_START + $n * ($n-1) ))

# :/
# echo $(( $n ** 3 ))
