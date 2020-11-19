class Solution {
public:
    string intToRoman(int num) {
        vector<vector<char>> vvc(5, vector<char>(2));
        vvc[4] = {'M', '!'};
        vvc[3] = {'C', 'D'};
        vvc[2] = {'X', 'L'};
        vvc[1] = {'I', 'V'};
        
        string ans = "";
        while (num) {
            string strNum = to_string(num);
            int digit = strNum[0] - '0';
            int len = strNum.length();
            if (digit % 5 == 4) {
                num += 1 * pow(10, len - 1);
                ans += vvc[len][0];
            }
            else if (digit >= 5) {
                num -= 5 * pow(10, len - 1);
                ans += vvc[len][1];
            }
            else {
                num -= 1 * pow(10, len - 1);
                ans += vvc[len][0];
            }
        }
        
        return ans;
    }
};