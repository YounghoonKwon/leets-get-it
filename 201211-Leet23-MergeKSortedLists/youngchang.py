# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
heap = []
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lists = [i for i in lists if i]
        if not heap:
            for i in lists:
                heapq.heappush(heap, i.val)
        if not lists: return None
        dummy = ListNode()
        d = dummy
        min_val = heapq.heappop(heap)
        for i in range(len(lists)):
            if lists[i].val == min_val:
                d.next = lists[i]
                d = d.next
                lists[i] = lists[i].next
                if lists[i]:
                    heapq.heappush(heap, lists[i].val)
                break
        d.next = self.mergeKLists(lists)
        return dummy.next