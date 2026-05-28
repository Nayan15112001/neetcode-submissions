# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverse(l):
            curr,prev = l,None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        rev = reverse(head) 
        curr,prev = rev,None
        pos = 1
        if n == 1:
            curr = curr.next
            return reverse(curr)
        while curr:
            if pos!= n:
                prev = curr
                curr = curr.next
                pos+=1
            else:
                prev.next = curr.next
                return reverse(rev)
        return head


        