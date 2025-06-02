# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

# 解題思路：
# 將兩個 linked list 視為反向數字，每位做加總並處理進位。
# 使用 dummy head 建立新 linked list 結果，邊走邊加。

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
