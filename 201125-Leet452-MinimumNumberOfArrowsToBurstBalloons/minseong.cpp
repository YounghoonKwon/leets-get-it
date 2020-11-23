class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        if (points.size() == 0) return 0;
        
        int ans = 1;
        int minEndPoint = points[0][1];
        
        sort(begin(points), end(points));
        
        for (auto& point : points) {
            if (point[0] > minEndPoint) {
                minEndPoint = point[1];
                ans += 1;
            }
            if (point[1] < minEndPoint) {
                minEndPoint = point[1];
            }
        }
        
        return ans;
    }
};