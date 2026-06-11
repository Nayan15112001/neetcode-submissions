# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True

        if p == None and q:
            return False
        
        if q == None and p:
            return False
        
        q1 = deque()
        if p and q:
            q1.append((p,q))
        
        print(q1)
        
        while q1 :
            p_node,q_node = q1.popleft()
            if p_node.val != q_node.val:
                return False
            if p_node.left: 
                if not q_node.left:
                    return False
                q1.append((p_node.left,q_node.left))
            if p_node.right: 
                if not q_node.right:
                    return False
                q1.append((p_node.right,q_node.right))
            if q_node.left:
                if not p_node.left:
                    return False
            if q_node.right:
                if not p_node.right:
                    return False
            
    
        return True



            