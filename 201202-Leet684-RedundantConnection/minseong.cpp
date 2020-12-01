class Solution {
public:
    
    int maxx = -1;
    vector<vector<int>> fromTo;
    unordered_map<int, int> order;
    
    bool findCycle(bool* vis, int cur, int prv, stack<pair<int, int>>& footPrint)
    {
        if (vis[cur]) {
            while (true) {
                int hash = footPrint.top().first * 2000 + footPrint.top().second;
                if (maxx < order[hash]) {
                    maxx = order[hash];
                }
                if (footPrint.top().first == cur) {
                    return true;
                }
                footPrint.pop();
            }
        }
        
        vis[cur] = true;
        for (int to : fromTo[cur]) {
            if (to != prv) {
                footPrint.push({cur, to});
                if (findCycle(vis, to, cur, footPrint)) return true;
                footPrint.pop();
            }
        }
        vis[cur] = false;
        
        return false;
    }
    
    vector<int> findRedundantConnection(vector<vector<int>>& edges)
    {
        fromTo.resize(edges.size() + 1);
        for (int i = 0; i < edges.size(); ++i) {
            order[edges[i][0] * 2000 + edges[i][1]] = i;
            order[edges[i][1] * 2000 + edges[i][0]] = i;
            fromTo[edges[i][0]].push_back(edges[i][1]);
            fromTo[edges[i][1]].push_back(edges[i][0]);
        }
        
        bool* vis = new bool[edges.size() + 1]{false, };
        stack<pair<int, int>> footPrint;
        findCycle(vis, 1, -1, footPrint);
        return edges[maxx];
    }
};