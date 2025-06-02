# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/

# 解題思路：
# 

class Solution:
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]
