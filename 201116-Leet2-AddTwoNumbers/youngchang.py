# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        q = 0
        curr = dummy
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            s = a + b + q
            
            q, r = divmod(s, 10)
            curr.next = ListNode(r)
            curr = curr.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        if q:
            curr.next = ListNode(q)
            
        return dummy.next