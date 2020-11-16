class Solution {
public:
    
    long long reverseNumber(long long num) {
        bool isMinus = false;
        if (num < 0) {
            isMinus = true;
            num *= -1;
        } 
        
        long long result = 0;
        while (num) {
            result = result * 10 + num % 10;
            num /= 10;
        }
        
        return isMinus ? result * -1 : result;
    }
    
    int reverse(int x) {
        long long ans = reverseNumber(x);
        
        if (ans > INT_MAX || ans < INT_MIN) {
            return 0;
        }
        else {
            return ans;
        }
    }
};