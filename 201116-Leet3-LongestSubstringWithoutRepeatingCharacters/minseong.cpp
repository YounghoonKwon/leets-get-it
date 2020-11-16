class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int ans = 0;
        unordered_map<char, int> cntum;
        for (int left = 0, right = 0; right < s.size(); ++right) {
            char rightChar = s[right];
            cntum[rightChar] += 1;
            while (cntum[rightChar] > 1) {
                char leftChar = s[left++];
                cntum[leftChar] -= 1;
            }
            ans = max(ans, right - left + 1);
        }
        
        return ans;
    }
};