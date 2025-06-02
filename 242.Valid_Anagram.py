# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/

# 解題思路：
# 

class Solution:
    def isAnagram(self, s, t):
            return sorted(s) == sorted(t)
