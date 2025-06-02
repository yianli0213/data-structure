# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/

# 解題思路：
# 

class Solution:
    def hasCycle(self, head):
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return True
            return False
