# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse_linked_list(self, l1):
            curr,prev = l1,None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        fast = head
        slow = head
        prev = None
        while fast and fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next
        
        l2 = slow.next
        slow.next = None
        l2 = reverse_linked_list(self,l2)
        
        l1 = head
        temp1,temp2 = None,None
        while l1 and l2:
            temp1 = l1.next
            temp2 = l2.next 
            l1.next = l2
            l2.next = temp1
            l1 = temp1
            l2 = temp2
        

    



        


