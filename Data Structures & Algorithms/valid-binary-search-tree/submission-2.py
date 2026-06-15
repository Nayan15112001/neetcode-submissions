# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         val = val
#         left = left
#         right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        low = float('-inf')
        high = float('inf')
        def dfs(node,low,high):
            if not node:
                return True
            if node.val<=low or node.val>=high:
                return False
            return (dfs(node.left,low,node.val) and dfs(node.right,node.val,high))
            
            
        return dfs(root,low,high)


