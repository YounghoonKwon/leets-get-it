class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        size = len(prices)
        hold = [0]*size
        unhold = [0]*size
        hold[0] = -prices[0]
        for i in range(1,size):
            hold[i] = max(unhold[i-1]-prices[i], hold[i-1])
            unhold[i] = max(hold[i-1]+prices[i]-fee, unhold[i-1])
        return unhold[-1]
        
