class Solution {
public:
    string removeKdigits(string num, int k) {
        int n = num.length();
        string ans = "";
        vector<int> counts(10);
        int needed = n - k;
        auto goOn = [&](int& i, int diff) { counts[num[i] - '0'] += diff, ++i; };
        
        for (int l = 0, r = 0; needed; needed--) {
            while (r <= n - needed) goOn(r, 1);
            
            int i = -1;
            while (!counts[++i]) ;
            ans += i + '0';
            if (ans[0] == '0') ans.pop_back();
            
            while (num[l] - '0' != i) goOn(l, -1);
            goOn(l, -1);
        }
        
        return ans.empty() ? "0" : ans;
    }
};