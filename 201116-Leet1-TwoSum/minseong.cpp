class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numToIndex;
        
        for (int i = 0; i < nums.size(); ++i) {
            int neededNumber = target - nums[i];
            if (numToIndex.find(neededNumber) != numToIndex.end()) {
                return {numToIndex[neededNumber], i};
            }
            else {
                numToIndex[nums[i]] = i;
            }
        }
        
        return {};
    }
};