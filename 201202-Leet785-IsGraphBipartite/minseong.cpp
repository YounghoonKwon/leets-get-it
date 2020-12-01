// beat 98.32% Runtime
class Solution {
public:
    bool isBipartite(vector<vector<int>>& graph) {
        vector<int> vertexs(graph.size());
        queue<int> q;
        for (int i = 0; i < graph.size(); ++i) {
            if (vertexs[i]) continue;
            
            vertexs[i] = 1;
            q.push(i);
            while (q.size()) {
                int cur = q.front(); q.pop();
                int nextSide = vertexs[cur] == 1 ? 2 : 1;

                for (int to : graph[cur]) {
                    if (vertexs[to] == 0) {
                        vertexs[to] = nextSide;
                        q.emplace(to);
                    }
                    else if (vertexs[to] == vertexs[cur]) {
                        return false;
                    }
                }
            }
        }
        
        return true;
    }
};

static const auto __ = []() {
    ios::sync_with_stdio(false);
    return 1;
}();