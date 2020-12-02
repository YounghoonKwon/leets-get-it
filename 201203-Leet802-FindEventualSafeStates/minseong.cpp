using usi = unordered_set<int>;
class Solution {
public:
    int* dp;
    int checkCycle(vector<vector<int>>& graph, usi& vis, int cur) {
        if (vis.count(cur)) {
            return 2;
        }
        if (dp[cur]) {
            return dp[cur];
        }
        
        dp[cur] = 1;
        vis.insert(cur);
        for (int i = 0; i < graph[cur].size(); ++i) {
            int result = checkCycle(graph, vis, graph[cur][i]);
            if (result == 2) {
                return dp[cur] = 2;
            }
        }
        vis.erase(cur);
        
        return dp[cur];
    }
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int n = graph.size();
        dp = new int[n]{0, };
        unordered_set<int> vis;
        for (int i = 0; i < n; ++i) {
            vis.clear();
            if (!dp[i]) {
                checkCycle(graph, vis, i);
            }
        }
        
        vector<int> ans;
        for (int i = 0; i < n; ++i) {
            if (dp[i] == 1) {
                ans.push_back(i);
            }
        }
        return ans;
    }
};

static const auto __ = []() {
    ios::sync_with_stdio(false);
    return 1;
}();