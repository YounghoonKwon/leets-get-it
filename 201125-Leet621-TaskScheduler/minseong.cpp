class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> vec(27);
        for (auto task : tasks) {
            vec[task-'A'] += 1;
        }
        
        sort(begin(vec), end(vec), greater<int>());
        
        int ans = 0;
        while (vec.size()) {
            int i = 0;
            for (; vec[i] && i <= n; ++i) {
                vec[i] -= 1;
            }
            sort(begin(vec), end(vec), greater<int>());
            while (vec.size() && vec.back() == 0) vec.pop_back();
            ans += vec.empty() ? i : n + 1;
        }
        
        return ans;
    }
};
