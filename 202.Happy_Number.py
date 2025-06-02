# 202. Happy Number
# https://leetcode.com/problems/happy-number/

# 解題思路：
# 

class Solution:
    def isHappy(self, n):
            def get_next(n):
                return sum(int(x) ** 2 for x in str(n))
            seen = set()
            while n != 1 and n not in seen:
                seen.add(n)
                n = get_next(n)
            return n == 1
