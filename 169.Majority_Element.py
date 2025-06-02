# 169. Majority Element
# https://leetcode.com/problems/majority-element/

# 解題思路：
# 

class Solution:
    def majorityElement(self, nums):
            count = 0
            candidate = None
            for num in nums:
                if count == 0:
                    candidate = num
                count += (1 if num == candidate else -1)
            return candidate
