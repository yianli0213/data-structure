# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/

# 解題思路：
# 

class Solution:
    def containsDuplicate(self, nums):
            return len(nums) != len(set(nums))
