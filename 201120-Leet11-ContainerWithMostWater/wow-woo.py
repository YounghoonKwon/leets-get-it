class Solution:
    def maxArea(self, height: List[int]) -> int:
        vol = 0
        
        i, j = 0, len(height) - 1
        while i < j:
            vol = max(vol, (j - i) * min(height[i], height[j]))
            i1, j1 = i, j
            if height[i] <= height[j]:
                i1 += 1
                while i1 < j and height[i1] <= height[i]:
                    i1 += 1
            if height[i] >= height[j]:
                j1 -= 1
                while j1 > i1 and height[j1] <= height[j]:
                    j1 -= 1
            
            i, j = i1, j1
        
        return vol
