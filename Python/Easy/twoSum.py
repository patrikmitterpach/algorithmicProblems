def twoSum(nums, target):
        dictionary = {}

        for idx, num in enumerate(nums):
            numberToTarget = target - num
            if numberToTarget in dictionary:
                return [dictionary[numberToTarget], idx]
            dictionary[num] = idx

print( twoSum([2,7,11,15], 9) )