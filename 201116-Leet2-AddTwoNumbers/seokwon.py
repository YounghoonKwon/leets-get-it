# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        twosum = 0
        exp = 0
        ten = 10
        while l1 or l2:
            if l1:
                twosum += (ten**exp)*l1.val
                l1 = l1.next
            if l2:
                twosum += (ten**exp)*l2.val
                l2 = l2.next
            exp +=1
            print('-'*20)
        return makingReturnNode(twosum)
        

def makingReturnNode(inputValue : int):
    eachNum = convert_Int_To_List(inputValue)
    result = None
    for i in eachNum:
        Node = ListNode(i,result)
        result = Node
    return result
    
def convert_Int_To_List(inte : int) ->list:
    res = [int(x) for x in str(inte)]
    return res
