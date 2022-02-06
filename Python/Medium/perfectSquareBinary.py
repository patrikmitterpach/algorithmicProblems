# Given a positive integer num,
#  write a function which returns True
#  if num is a perfect square else False.
# Follow up: 
#   Do not use any built-in library function such as sqrt.

# Done in Easy in an O( sqrt(n) ) complexity, however binary search can
#   also be utilised for better performance


def isPerfectSquare(num: int) -> bool:
    start: int = 0
    end: int = num

    while start <= end:
        middle: int = int((start + end) // 2)
        middleSquared = middle*middle
        # print(start, middle, end  )
        if middleSquared < num:
            start = middle + 1
        elif middleSquared > num:
            end = middle - 1
        else:
            return True
    return False

for i in range(1000000):
    assert( isPerfectSquare(697) == False)

newList = [num for num in range(1000)]
map(print, newList)