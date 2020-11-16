class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.sort()
        nums2.sort()
        total_len = len(nums1) + len(nums2)
        def findKth(idx, is_odd):
            result = []
            while idx >= 0:
                idx -= 1
                if not nums1 and nums2:
                    result.append(nums2.pop(0))
                    continue
                if not nums2 and nums1:
                    result.append(nums1.pop(0))
                    continue
                if nums1[0] > nums2[0]:
                    result.append(nums2.pop(0))
                else:
                    result.append(nums1.pop(0))
            return result[len(result)-1] if is_odd else (result[len(result)-1]+result[len(result)-2])/2

        result = None
        if total_len % 2 == 1:
            result = findKth(total_len//2, True)
        else:
            result = findKth(total_len//2, False)
        return result
        
        
