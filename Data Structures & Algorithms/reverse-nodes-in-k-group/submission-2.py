# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self,l,r):
        curr = l
        prev = None
        while curr!=r:
            temp  = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev,l
       

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        gp = dummy
        dummy.next = head
        gs = ge = ng = head
        count = 1
        while ge:
            if count%k == 0:
                ng = ge.next
                gs,ge = self.reverse(gs,ng)
                gp.next = gs

                gp = ge
                ge.next = ng
                ge = ge.next
                gs = ge
            else:
                ge = ge.next
            
            count+=1

        return dummy.next
            
        