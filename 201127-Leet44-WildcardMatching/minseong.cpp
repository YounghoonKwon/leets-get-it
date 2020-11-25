class Solution {
public:
    bool isMatch(string s, string p) {
        int n = s.size();
        int m = p.size();
        s.push_back('!');
        vector<vector<bool>> dp(n + 2, vector<bool>(m + 1));
        
        dp[0][0] = true;
        for (int i = 0; i <= n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (dp[i][j] == false) {
                    continue;
                }
                
                if (p[j] == '*') {
                    dp[i][j+1] = dp[i+1][j] = true;
                }
                else if (p[j] == '?' || s[i] == p[j]) {
                    dp[i+1][j+1] = true;
                }
            }
        }
        
        return dp[n][m];
    }
};