# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

# 解題思路：
# 

class Solution:
    def reverseList(self, head):
            prev = None
            current = head
            while current:
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt
            return prev
