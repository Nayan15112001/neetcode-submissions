# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.s = ''
        def dfs(root):
            if not root:
                self.s+=  'none' + ','
                return 
            self.s+=   str(root.val) + ','
            return dfs(root.left) or dfs(root.right)
        dfs(root)
        print(self.s)
        return self.s
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.i = 0
        arr = data.split(',')
        def dfs():
            val = arr[self.i]
            if val == 'none':
                return
            root = TreeNode(int(val))
            self.i+=1
            root.left = dfs()
            root.right = dfs()
        dfs()
        return root
