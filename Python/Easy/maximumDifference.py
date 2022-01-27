def maximumDifference(nums):
    
    maxDiff = -1
    minNum = nums[0]
    maxNum = nums[0]

    for idx, num in enumerate(nums):
        if num < minNum:
            minNum = num
            maxNum = num
        if num > maxNum:
            maxNum = num

        if maxNum - minNum > maxDiff and maxNum != minNum:
            maxDiff = maxNum - minNum

    return maxDiff

print(maximumDifference( [9,4,3,2] ))    
