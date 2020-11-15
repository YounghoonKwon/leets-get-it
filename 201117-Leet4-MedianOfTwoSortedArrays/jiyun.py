class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        sumed = nums1 + nums2
        sort = sorted(sumed)
        if len(sumed) % 2 != 0:
            return float(sort[len(sumed)/2])
        else:
            return float(sort[len(sumed)/2-1]+sort[len(sumed)/2])/float(2)
