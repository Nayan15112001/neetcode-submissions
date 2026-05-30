# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def fetch_number(l):
            curr= l
            i = sum = 0
            while curr:
                sum += curr.val * 10**i
                curr = curr.next
                i+=1
            return sum
        num1 = fetch_number(l1)
        num2 = fetch_number(l2)
        total = num1+num2
        print(total)
        l = ListNode()
        curr = l
        if total == 0:
            return ListNode()
        while total:
            digit = total%10
            print(digit)
            x = ListNode(digit)
            l.next = x
            print(l.next.val)
            total = total//10
            l = l.next
        return curr.next

