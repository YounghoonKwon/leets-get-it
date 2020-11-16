# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = sum = ListNode(0)
        print('sum', sum)
        bonus = 0
        while True:
            sum_current = l1.val + l2.val + bonus
            bonus = 0
            if sum_current > 9:
                sum_current = sum_current % 10
                bonus = 1

            sum.val = sum_current

            if not l1.next and not l2.next:
                if bonus == 1:
                    sum.next = ListNode(1)
                break
            elif l1.next and not l2.next:
                l1 = l1.next
                l2 = ListNode(0)
                l2.val = 0
            elif not l1.next and l2.next:
                l1 = ListNode(0)
                l1.val = 0
                l2 = l2.next
            else:
                l1 = l1.next
                l2 = l2.next
            sum.next = ListNode(0)
            sum = sum.next

        return result
