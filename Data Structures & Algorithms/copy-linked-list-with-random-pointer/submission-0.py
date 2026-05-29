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
        copy = Node(-1)
        new = copy
        hmap= {}
        while curr:
            new.next = Node(curr.val)
            hmap[curr] = new.next
            curr = curr.next
            new = new.next
        copy = copy.next
        
    # assigning the next and random pointers to the new list    
        curr = head
        new = copy
        while curr:

            if curr.next in hmap:
                new.next = hmap[curr.next]
            else:
                new.next = None

            if curr.random in hmap:
                new.random = hmap[curr.random]
            else:
                new.random = None
            new = new.next
            curr = curr.next
        return copy


            
            
            