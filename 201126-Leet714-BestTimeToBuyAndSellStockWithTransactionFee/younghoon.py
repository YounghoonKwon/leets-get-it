class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit, buy = 0, float('inf')
        for x in prices:
            buy = min(buy, x-profit+fee)
            profit = max(profit,x-buy)
        return profit
