class Solution {
public:
    bool isPossible(vector<int>& nums) {
        unordered_map<int, int> need;
        
        for (int i = 0, j = 0; i < nums.size(); ++i) {
            need[nums[i]] -= 1;
            
            while (nums[j] < nums[i] - 1) ++j;
            
            if (nums[j] == nums[i] - 1) {
                ++j;
            }
            else {
                need[nums[i] + 1] += 1;
                need[nums[i] + 2] += 1;
            }
            
        }
        
        for (auto pr : need) {
            if (pr.second > 0) {
                return false;
            }
        }
        
        return true;
    }
};

static const auto speedUpIO = []() {
    ios::sync_with_stdio(false);
    return 1;
}();