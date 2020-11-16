class Solution {
public:
    int romanToValue[100];
    
    Solution() {
        romanToValue['I'] = 1;
        romanToValue['V'] = 5;
        romanToValue['X'] = 10;
        romanToValue['L'] = 50;
        romanToValue['C'] = 100;
        romanToValue['D'] = 500;
        romanToValue['M'] = 1000;
    }
    
    int romanToInt(string s) {
        reverse(begin(s), end(s));
        char maxRoman = 'I';
        
        int ans = 0;
        for (char roman : s) {
            if (romanToValue[roman] < romanToValue[maxRoman]) {
                ans -= romanToValue[roman];
            }
            else {
                ans += romanToValue[roman];
            }
            
            if (romanToValue[maxRoman] < romanToValue[roman]) {
                maxRoman = roman;
            }
        }
        
        return ans;
    }
};