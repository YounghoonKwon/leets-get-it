// beat 100% Runtime
// beat 90.41% Memory Usage
using Trans = unordered_map<string, int>;
using Edges = vector<vector<pair<int, double>>>;

class Solution {
public:
    double bfs(Edges& edges, int from, int dest) {
        vector<int> vis(41);
        queue<pair<int, double>> q;
        q.push({from, 1});
        vis[from] = true;
        
        while (q.size()) {
            int curName = q.front().first;
            double curValue = q.front().second;
            q.pop();
            for (auto& to : edges[curName]) {
                if (vis[to.first]) {
                    continue;
                }
                vis[to.first] = true;
                double nextValue = curValue * to.second;
                if (to.first == dest) {
                    return nextValue;
                }
                q.push({to.first, nextValue});
            }
        }
        
        return -1;
    }
    
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        Trans names;
        Edges edges(41);
        for (int i = 0, name = 1; i < equations.size(); ++i) {
            for (int j = 0; j < 2; ++j) {
                if (!names[equations[i][j]]) {
                    names[equations[i][j]] = name++;
                }
            }
            int left = names[equations[i][0]];
            int right = names[equations[i][1]];
            edges[left].push_back({right, values[i]});
            edges[right].push_back({left, (double)1 / values[i]});
        }
        
        vector<double> ans;
        for (auto& query : queries) {
            int left = names[query[0]];
            int right = names[query[1]];
            if (!left || !right) {
                ans.push_back(-1);
            }
            else if (left == right) {
                ans.push_back(1);
            }
            else {
                ans.push_back(bfs(edges, left, right));
            }
        }
        
        return ans;
    }
};