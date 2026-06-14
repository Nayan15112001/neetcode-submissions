# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        dq = deque()
        l = []
        if not root:
            return []
        dq.append(root)
        while dq:
            dq_size = len(dq)
            last_node = dq[-1]
            l.append(last_node.val)
            for i in range(dq_size):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return l
