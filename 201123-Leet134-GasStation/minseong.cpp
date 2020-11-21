class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int n = gas.size();
        
        int minSum = 0;
        int minx = 0;
        int sum = 0;
        for (int i = 0; i < n; ++i) {
            sum += gas[i];
            sum -= cost[i];
            if (sum < minSum) {
                minSum = sum;
                minx = (i + 1) % n;
            }
        }
        
        return sum >= 0 ? minx : -1;
    }
};