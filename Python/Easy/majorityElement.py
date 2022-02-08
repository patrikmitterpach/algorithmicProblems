# Leetcode #169
# Given an array nums of size n, return the majority element.
#  The majority element is the element that appears more than ⌊n / 2⌋ times.
#  You may assume that the majority element always exists in the array.

# O(n * log(n) ) solution
# Sort the array, return the element on the middle position
# LeetCode runtime of 262 ms
def majorityElementSort(nums):
    nums.sort()
    return nums[len(nums) // 2]

# O(n/2 * n)
# Terribly inefficient, for every number the entire arr gets looked at
# LeetCode runtime exceeded
def majorityElementCount(nums):
    halfLength = len(nums) // 2
    for num in nums:
        if nums.count(num) > halfLength:
            return num

# O(n) with O(n) space
def majorityElementHash(nums):
    hashMap = {}
    result, maxCount = 0

    for num in nums:
        hashMap[num] = 1 + hashMap.get(num)
        result = num if hashMap[num] > maxCount else result
        maxCount = max(hashMap[num], maxCount)

    return result