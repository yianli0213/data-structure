# 136. Single Number
# https://leetcode.com/problems/single-number/

# 解題思路：
# 

class Solution:
    def singleNumber(self, nums):
            result = 0
            for num in nums:
                result ^= num
            return result
