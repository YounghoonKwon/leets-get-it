class Solution:
    def maxArea(self, height: List[int]) -> int:
        #edge case
        if len(height) == 2:
            return min(height)
        dp={}
        
        for i in range(len(height)-1):
            for j in range(i+1, len(height)):
                dis = abs(i-j)
                #Avoiding duplicates
                current = min(height[i], height[j])
                if dis in dp:
                    dp[dis] = max(dp[dis], current)
                else:
                    dp[dis] = current
        result = 0
        for item in dp:
            current = item * dp[item]
            result = max(result, current)
        return result
