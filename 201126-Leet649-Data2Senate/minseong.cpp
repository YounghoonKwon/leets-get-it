class Solution {
public:
    string predictPartyVictory(string senate) {
        queue<int> R;
        queue<int> D;
        
        for (int i = 0; i < senate.size(); ++i) {
            if (senate[i] == 'R') {
                R.push(i);
            }
            else {
                D.push(i);
            }
        }
        
        int trackIndex = R.size() + D.size();
        while (R.size() && D.size()) {
            if (R.front() < D.front()) {
                R.push(trackIndex++);
            }
            else {
                D.push(trackIndex++);
            }
            D.pop();
            R.pop();
        }
        
        return R.size() ? "Radiant" : "Dire";
    }
};

static const auto speedUpIO = []() {
    ios::sync_with_stdio(false);
    return 1;
}();