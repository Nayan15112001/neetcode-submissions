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
        def dfs(root,low,high):
            if not root:
                return True
            
            if root.val<=low or root.val>=high:
                return False
            
            return dfs(root.left,low,root.val) and dfs(root.right,root.val,high)
        return dfs(root,low,high)
