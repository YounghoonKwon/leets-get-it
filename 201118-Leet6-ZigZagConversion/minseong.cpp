class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1) {
            return s;
        }
        
        vector<string> lines(numRows, "");
        int go = 1;
        int edge = numRows - 1;
        for (int i = 0, line = 0; i < s.size(); ++i) {
            lines[line] += s[i];
            if (i && i % edge == 0) {
                go *= -1;
            }
            line += go;
        }
        
        string ans = "";
        for (auto& line : lines) {
            ans += line;
        }
        return ans;
    }
};