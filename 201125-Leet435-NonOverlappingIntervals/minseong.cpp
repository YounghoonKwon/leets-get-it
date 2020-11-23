class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        if (intervals.size() == 0) return 0;
        
        sort(begin(intervals), end(intervals), [](const auto& l, const auto& r) {
            return l[1] == r[1] ? l[0] > r[0] : l[1] < r[1];
        });
        
        int ans = intervals.size();
        int prvEndPoint = -2e9;
        for (auto& interval : intervals) {
            if (interval[0] >= prvEndPoint) {
                ans -= 1;
                prvEndPoint = interval[1];
            }
        }
        return ans;
    }
};