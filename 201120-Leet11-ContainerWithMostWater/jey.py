class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
 
        # 1. Brute Force
        max_water = 0
        n = len(height)
 
        for i in range(n) :
            for j in range(i+1, n) :
                max_water = max((j-i)*min(height[i], height[j]), max_water)
 
        return max_water

