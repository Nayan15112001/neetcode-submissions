# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        curr = head
        for i in range(1,n):
            curr = curr.next
        fast = curr
        slow_prev = None
        while fast and fast.next:
            slow_prev = slow
            slow = slow.next
            fast = fast.next
        if slow_prev:
            slow_prev.next = slow.next
        else:
            head = head.next
        return head
        

            


        