class Solution {
public:
    int dfs(vector<vector<int>>& fromTo, vector<vector<int>>& maxs, int cur, int prv) {
        for (int to : fromTo[cur]) {
            if (to == prv) continue;
            
            int result = dfs(fromTo, maxs, to, cur) + 1;
            if (result > maxs[cur][0]) {
                maxs[cur][1] = maxs[cur][0];
                maxs[cur][0] = result;
            }
            else if (result > maxs[cur][1]) {
                maxs[cur][1] = result;
            }
        }
        return maxs[cur][0];
    }
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        if (edges.size() == 0) {
            return {0};
        }
        
        vector<vector<int>> maxs(n + 1, {1, 1});
        vector<vector<int>> fromTo(n);
        for (auto& edge : edges) {
            fromTo[edge[0]].push_back(edge[1]);
            fromTo[edge[1]].push_back(edge[0]);
        }
        
        dfs(fromTo, maxs, 0, -1);
        
        maxs[n][0] = maxs[n][1] = -1;
        queue<pair<int, int>> q;
        q.push({0, n});
        vector<int> ans;
        int minx = 1e9;
        while (q.size()) {
            int cur = q.front().first;
            int prv = q.front().second;
            q.pop();
            int curMax = maxs[cur][0];
            int prvMax = maxs[prv][0] == curMax + 1 ? maxs[prv][1] + 1 : maxs[prv][0] + 1;
            
            if (maxs[cur][0] < prvMax) {
                maxs[cur][1] = maxs[cur][0];
                maxs[cur][0] = prvMax;
            }
            else if (maxs[cur][1] < prvMax) {
                maxs[cur][1] = prvMax;
            }
            
            if (maxs[cur][0] < minx) {
                ans.clear();
                minx = maxs[cur][0];
                ans.push_back(cur);
            }
            else if (maxs[cur][0] == minx) {
                ans.push_back(cur);
            }
            
            for (int to : fromTo[cur]) {
                if (to != prv) {
                    q.push({to, cur});
                }
            }
        }
        
        return ans;
    }
};

static const auto speedUpIO = []() {
    ios::sync_with_stdio(false);
    return 1;
};