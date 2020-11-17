class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size() == 0) {
            return "";
        }
        
        int maxStringIndex = 0;
        for (int i = 0; i < strs.size(); ++i) {
            if (strs[maxStringIndex].size() < strs[i].size()) {
                maxStringIndex = i;
            }
        }
        
        string ans = "";
        for (int i = 0; ; ++i) {
            for (auto& str : strs) {
                if (i >= str.size() || strs[maxStringIndex][i] != str[i]) {
                    return ans;
                }
            }
            ans += strs[maxStringIndex][i];
        }
        
        return ans;
    }
};