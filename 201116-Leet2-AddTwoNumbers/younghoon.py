# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = out = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            twosum = 0
            if l1:
                twosum += l1.val
                l1 = l1.next
            if l2:
                twosum += l2.val
                l2 = l2.next
            if carry == 1:
                twosum += 1
            carry, value = divmod(twosum, 10)
            head.next = ListNode(value)
            head = head.next
        return out.next
            
