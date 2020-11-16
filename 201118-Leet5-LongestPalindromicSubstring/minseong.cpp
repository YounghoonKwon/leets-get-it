class Solution {
public:
    string longestPalindrome(string s) {
        int count = 0;
        int left = -1;
        int n = s.size();
        for (int i = 0; i < n; ++i) {
            int j = 1;
            while (i - j >= 0 && i + j < n && s[i-j] == s[i+j]) ++j;
            --j;
            if (2 * j + 1 > count) {
                left = i - j;
                count = 2 * j + 1;
            }
            
            j = 1;
            while (i - j + 1 >= 0 && i + j < n && s[i-j+1] == s[i+j]) ++j;
            --j;
            if (j * 2 > count) {
                left = i - j + 1;
                count = j * 2;
            }
        }
        
        return s.substr(left, count);
    }
};