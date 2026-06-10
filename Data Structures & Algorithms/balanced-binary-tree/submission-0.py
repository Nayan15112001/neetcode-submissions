# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True
        def dfs(root):
            if not root:
                return 0
            
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)

            print(f"left_depth:{left_depth}")
            print(f"right_depth:{right_depth}")
            if abs(left_depth-right_depth)>1:
                self.is_balanced  = False

            return 1 + max(left_depth,right_depth)
        dfs(root)
        

        return self.is_balanced