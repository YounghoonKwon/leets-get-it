class Solution {
public:
    vector<vector<int>> ans;
    int target;
    void dfs(vector<vector<int>>& graph, vector<int>& path, int prv) {
        if (path.back() == target) {
            ans.emplace_back(path);
            return;
        }
        
        for (int to : graph[path.back()]) {
            if (to != prv) {
                path.emplace_back(to);
                dfs(graph, path, path.back());
                path.pop_back();
            }
        }
    }
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        target = graph.size() - 1;
        vector<int> path;
        path.emplace_back(0);
        dfs(graph, path, -1);
        return ans;
    }
};