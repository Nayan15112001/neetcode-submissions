# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        n = len(lists)
        if n==0:
            return None
        for i in range(1,n):
            lists[i] = self.mergelist(lists[i-1],lists[i])
            # self.printlinkedlist(lists[i])
        return lists[-1]
        

    # def printlinkedlist(self,l):
    #     current = l
    #     arr = []
    #     while current:
    #         arr.append(current.val)
    #         current = current.next

    #     print(arr)
    
    def mergelist(self,l1,l2):
        head = ListNode()
        curr = head

        while l1 and l2:
            if l2.val<l1.val:
                curr.next = l2
                curr = curr.next
                l2 = l2.next
            else:
                curr.next = l1
                curr = curr.next
                l1 = l1.next
            
        if l1:
            curr.next = l1
        
        if l2:
            curr.next = l2
        return head.next
        
