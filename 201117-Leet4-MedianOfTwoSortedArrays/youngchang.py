class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        
        left = 0
        right = m
        while left <= right:
            x_idx = (left + right) // 2
            y_idx = (m + n) // 2 - x_idx
            
            x_left_max = -float('inf') if x_idx - 1 < 0 else nums1[x_idx - 1]
            y_left_max = -float('inf') if y_idx - 1 < 0 else nums2[y_idx - 1]
            
            x_right_min = float('inf') if x_idx >= m else nums1[x_idx]
            y_right_min = float('inf') if y_idx >= n else nums2[y_idx]
            
            left_max = max(x_left_max, y_left_max)
            right_min = min(x_right_min, y_right_min)
            
            if left_max > right_min:
                if x_left_max > y_right_min:
                    right = x_idx - 1
                elif y_left_max > x_right_min:
                    left = x_idx + 1
            else:
                if (m + n) % 2 == 1:
                    return right_min
                else:
                    return (left_max + right_min) / 2