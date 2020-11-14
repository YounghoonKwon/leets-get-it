# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = ListNode(0)
        temp  = root
        while l1 or l2:
            cur = 0
            if l1 != None:
                cur += l1.val
                l1 = l1.next

            if l2 != None:
                cur += l2.val
                l2 = l2.next
            cur += carry
            temp.next = ListNode(cur % 10)
            carry = 0
            
            if cur >= 10:
                carry = 1
            
            temp = temp.next
            
        if carry != 0:
            temp.next = ListNode(carry)
        return root.next
