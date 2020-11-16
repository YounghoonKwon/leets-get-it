class Solution {
public:
    bool isPalindrome(int x) {
        string strx = to_string(x);
        string rstrx = strx;
        reverse(begin(rstrx), end(rstrx));
        
        return strx.compare(rstrx) == 0;
    }
};