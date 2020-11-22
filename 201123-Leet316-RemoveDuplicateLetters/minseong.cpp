class Solution {
public:
    // beat 100%
    string removeDuplicateLetters(string s) {
        int n = s.size();
        int left = 0;
        for (char ch : s) {
            left |= 1 << (ch - 'a');
        }
        
        string ans = "";
        int leftCount = __builtin_popcount(left);
        for (int prvIndex = -1; leftCount; --leftCount) {
            int count = 0;
            char ch = ('z' + 1);
            int index = n;
            int appeared = 0;

            for (int i = n - 1; i > prvIndex; --i) {
                int bitMask = 1 << (s[i] - 'a');
                if (!(left & bitMask)) {
                    continue;
                }
                
                if(!(appeared & bitMask)) {
                    appeared |= bitMask;
                    count += 1;
                }
                if (s[i] <= ch && count == leftCount) {
                    index = i;
                    ch = s[i];
                }
            }

            ans += ch;
            left &= ~(1 << (ch - 'a'));
            prvIndex = index;
        }
        
        return ans;
    }
};