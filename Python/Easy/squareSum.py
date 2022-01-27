# Complete the square sum function so that it squares each
#  number passed into it and then sums the results together.

def squareSum(numbers):
    numbers = [num ** 2 for num in numbers]
    return sum(numbers)

print( squareSum([1,2,2]) )