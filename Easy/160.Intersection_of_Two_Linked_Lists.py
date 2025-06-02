# 160. Intersection of Two Linked Lists
# https://leetcode.com/problems/intersection-of-two-linked-lists/

# 解題思路：
# 

class Solution:
    def getIntersectionNode(self, headA, headB):
            if not headA or not headB:
                return None
            a, b = headA, headB
            while a != b:
                a = a.next if a else headB
                b = b.next if b else headA
            return a
