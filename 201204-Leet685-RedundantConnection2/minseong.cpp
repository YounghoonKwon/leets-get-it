class Solution {
public:
    static const int CYCLE = 1;
    static const int NOT_CYCLE = 2;
    vector<int> isCycle;
    vector<bool> vis;
    int dfs(vector<vector<int>>& fromTo, int cur) {
        if (vis[cur]) {
            return cur;
        }
        
        vis[cur] = true;
        for (int to : fromTo[cur]) {
            int result = dfs(fromTo, to);
            if (result) {
                vis[cur] = false;
                isCycle[cur] = CYCLE;
                return result == cur ? 0 : result;
            }
        }
        isCycle[cur] = NOT_CYCLE;
        vis[cur] = false;
        
        return 0;
    }
    
    vector<int> findRedundantDirectedConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        vector<vector<int>> fromTo(n + 1);
        vector<int> ans = {0, 0};
        for (int i = 0; i < n; ++i) {
            fromTo[edges[i][1]].push_back(edges[i][0]);
            if (fromTo[edges[i][1]].size() == 2) {
                ans = {edges[i][0], edges[i][1]};
            }
        }
        
        isCycle.resize(n + 1);
        vis.resize(n + 1);
        if (ans[0]) {
            int goTo1 = fromTo[ans[1]][0];
            int goTo2 = fromTo[ans[1]][1];
            dfs(fromTo, goTo1);
            dfs(fromTo, goTo2);
            if (isCycle[goTo1] == CYCLE) {
                return {goTo1, ans[1]};
            }
            else if (isCycle[goTo1] == CYCLE) {
                return {goTo2, ans[1]};
            }
            else {
                return ans;
            }
        }
        
        for (int i = 1; i <= n; ++i) {
            if (isCycle[i] == 0) {
                dfs(fromTo, i);
            }
        }
        
        for (int i = n - 1; i >= 0; --i) {
            if (isCycle[edges[i][0]] == CYCLE && isCycle[edges[i][1]] == CYCLE) {
                ans = {edges[i][0], edges[i][1]};
                break;
            }
        }
        
        return ans;
    }
};