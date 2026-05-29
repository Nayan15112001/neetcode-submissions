"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    # storing the old to new pointer mapping addresses
        curr = head
        hmap= {None:None}
        while curr:
            copy = Node(curr.val)
            hmap[curr] = copy
            curr = curr.next
            copy = copy.next
        
        
    # assigning the next and random pointers to the new list    
        curr = head
        while curr:
            new = hmap[curr]
            if curr.next in hmap:
                new.next = hmap[curr.next]
            else:
                new.next = None

            if curr.random in hmap:
                new.random = hmap[curr.random]
            else:
                new.random = None
            curr = curr.next
        return hmap[head]


            
            
            