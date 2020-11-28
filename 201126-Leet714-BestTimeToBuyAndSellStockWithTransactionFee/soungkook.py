class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        #   empty holding
        dp = [ [0,0] for _ in range(len(prices))]
        dp[0][0]=0
        dp[0][1]=-prices[0]-fee
        
        for i in range(1,len(prices)):
            dp[i][0], dp[i][1] = max(dp[i-1][0], dp[i-1][1] + prices[i]) , max(dp[i-1][0]-prices[i]-fee, dp[i-1][1])
        print('dp',dp)
        #return maximum benefit as you don't hold stack 
        return dp[-1][0]
