def twoSum(nums, target):
        for i in range( len(nums) ):
            for ii in range( len(nums) ):
                if nums[i] + nums[ii] == target and i != ii:
                    return [i, ii]
                    # Runtime O(n**2)

print( twoSum([2,7,11,15], 9) )