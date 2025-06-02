# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

# 思路：
# 使用堆疊（stack）儲存左括號，遇到右括號時比對是否匹配。
# 成對就彈出，不成對就直接 return False。
# 最後如果 stack 是空的，代表全部配對成功。

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

