class Solution {
public:
    bool isMatch(string s, string p) {
        int slen = s.size();
        int plen = p.size();
        vector<vector<bool>> dp(s.size() + 2, vector<bool>(p.size() + 1, false));
        
        s += "!";
        dp[0][0] = true;
        for (int i = 0; i <= slen; ++i) {
            for (int j = 0; j < p.size(); ++j) {
                if (dp[i][j] == false) {
                    continue;
                }
                
                
                if (p[j] >= 'a' && p[j] <= 'z') { // letter check
                    dp[i+1][j+1] = s[i] == p[j] ? true : dp[i+1][j+1];
                }
                else if (p[j] == '.') { // '.' definitely ok
                    dp[i+1][j+1] = true;
                }
                else { // '*' two cases occur 1. keep * 2. skip *
                    dp[i][j+1] = true;
                    dp[i+1][j] = s[i] == p[j-1] || p[j-1] == '.' ? true : dp[i+1][j];
                }
                
                if (j + 1 < p.size() && p[j+1] == '*') { // add p[j] letter 0 time
                    dp[i][j+2] = true;
                }
            }
        }
        
        return dp[slen][plen];
    }
};