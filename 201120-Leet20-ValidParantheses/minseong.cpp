class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> um;
        um[')'] = '(';
        um['}'] = '{';
        um[']'] = '[';
        
        stack<char> sStack;
        for (char ch : s) {
            if (um.find(ch) != um.end()) {
                if (sStack.empty() || sStack.top() != um[ch]) {
                    return false;
                }
                sStack.pop();
            }
            else {
                sStack.push(ch);
            }
        }
        
        return sStack.empty();
    }
};