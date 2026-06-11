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
        q1 = deque()
        q2 = deque()
        if p:
            q1.append(p)
        if q:
            q2.append(q)
        print(q1)
        print(q2)
        
        while q1 and q2:
            p_node = q1.popleft()
            q_node = q2.popleft()
            
            if p_node.val != q_node.val:
                return False
            if p_node.left: 
                if not q_node.left:
                    return False
                q1.append(p_node.left)
            if q_node.left: 
                if not p_node.left:
                    return False
                q2.append(q_node.left)
            if p_node.right: 
                if not q_node.right:
                    return False
                q1.append(p_node.right)
            if q_node.right: 
                if not p_node.right:
                    return False
                q2.append(q_node.right)

        if q2:
            return False
        if q1:
            return False
        
       
        return True



            