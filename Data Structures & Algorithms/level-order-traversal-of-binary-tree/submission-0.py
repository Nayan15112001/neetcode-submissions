# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans =[]
        l = []
        dq =deque()
        if not root:
            return []
        dq.append(root)
        
        while dq:

            level_size = len(dq)
            for i in range(level_size):
                node = dq.popleft()
                if node:
                    l.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            ans.append(l)
            l = []

        return ans