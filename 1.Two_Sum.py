# 1. Two Sum
# https://leetcode.com/problems/two-sum/

# 解題思路：
# 

class Solution:
    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i
