class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        li = nums1+nums2
        li.sort(reverse=False)
        if len(li) %2 != 0:
            return float(li[len(li)//2])
        else:
            return float((li[len(li)//2]+li[len(li)//2-1])/2)
            
