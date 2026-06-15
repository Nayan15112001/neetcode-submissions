# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_val = float('-inf')
        self.count = 0
        def dfs(node,max_val):
            if not node:
                return 0
            print(f'node :{node.val}')
            print(f'max_val:{max_val}')
            if node.val >= max_val:
                self.count+=1
                max_val = node.val
            if node.left:
                dfs(node.left,max_val)
            if node.right:
                dfs(node.right,max_val)
            return self.count
        return dfs(root,max_val)
            


            
