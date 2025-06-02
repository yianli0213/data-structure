# 94. Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/

# 思路：
# 使用 Stack 模擬遞迴過程：
# 1. 往左子樹一路推入 stack。
# 2. 沒左子樹時，pop 並加入結果。
# 3. 然後轉向右子樹，重複過程。

from typing import Optional, List

# 標準的 TreeNode 定義
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            res.append(current.val)
            current = current.right

        return res
