class Solution {
public:
    int maxArea(vector<int>& height) {
        int ans = 0;
        
        for (int l = 0, r = height.size() - 1; l < r;) {
            ans = max(ans, min(height[l], height[r]) * (r - l));
            
            if (height[r] > height[l]) l += 1;
            else if (height[l] > height[r]) r -= 1;
            else r -= 1, l += 1;
        }
        
        return ans;
    }
};