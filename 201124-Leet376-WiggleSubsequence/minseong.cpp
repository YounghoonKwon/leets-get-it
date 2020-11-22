class Solution {
public:
    // beat 100%
    int wiggleMaxLength(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;
        
        int ans = 1;
        for (int i = 0; i < n - 1;) {
            if (nums[i] < nums[i+1]) {
                while (i + 1 < n && nums[i] <= nums[i+1]) ++i;
                ans += 1;
            }
            else if (nums[i] > nums[i+1]) {
                while (i + 1 < n && nums[i] >= nums[i+1]) ++i;
                ans += 1;
            }
            else {
                ++i;
            }
        }
        
        return ans;
    }
};