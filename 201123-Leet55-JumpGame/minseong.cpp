class Solution {
public:
    bool canJump(vector<int>& nums) {
        for (int i = 0, left = 0; i < nums.size() - 1; ++i, --left) {
            left = max(left, nums[i]);
            if (!left) return false;
        }
        return true;
    }
};