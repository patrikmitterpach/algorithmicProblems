# The maximum sum subarray problem consists in finding the maximum 
#   sum of a contiguous subsequence in an array or list of integers.
# O(n^2)

def max_sequence(arr):
    maxVal = 0

    # For every element loop through every following element,
    #   save the highest running currSum to max
    for idx, num in enumerate(arr):
        currSum = 0
        
        for i in range(idx, len(arr)):
            currSum += arr[i]
            if currSum > maxVal:
                
                maxVal = currSum

    return maxVal

print( max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) )