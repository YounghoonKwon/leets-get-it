class Solution(object):
    def maxArea(self, height):
        if len(height) == 2:
            return min(height)
        
        start = 0
        end = len(height) - 1
        maxWater = 0

        for i in range(len(height)):
            width = abs(start - end)
            water = width * min(height[start], height[end])
            
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
                
            maxWater = max(water, maxWater)
            
        return maxWater
