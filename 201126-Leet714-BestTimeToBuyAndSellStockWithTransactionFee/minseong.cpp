// beat TC 99.93%, SC 98.98%
// dp solution
class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        int stockOnState = -2e9;
        int stockOffState = 0;
        int nextStockOnState = 0;
        int nextStockOffState = 0;
        
        for (int i = 0; i < prices.size(); ++i) {
            nextStockOnState = max(stockOnState, stockOffState - prices[i]);
            nextStockOffState = max(stockOffState, stockOnState + prices[i] - fee);
            
            stockOnState = nextStockOnState;
            stockOffState = nextStockOffState;
        }
        
        return stockOffState;
    }
};

static const auto __ = []() {
    ios::sync_with_stdio(false);
    return 1;
}();