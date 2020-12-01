using Vertex = unordered_map<string, vector<string>>;
class Solution {
public:
    bool dfs(Vertex& vertex, unordered_map<string, int>& ticketsLeft, vector<string>& ans, string cur, int count) {
        if (count == 0) {
            return true;
        }
        for (string& to : vertex[cur]) {
            string ticket = cur + "," + to;
            if (ticketsLeft[ticket] > 0) {
                ans.push_back(to);
                ticketsLeft[ticket] -= 1;
                if (dfs(vertex, ticketsLeft, ans, to, count - 1)) return true;
                ticketsLeft[ticket] += 1;
                ans.pop_back();
            }
        }
        return false;
    }
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        unordered_map<string, int> ticketsLeft;
        Vertex vertex;
        for (auto& ticket : tickets) {
            vertex[ticket[0]].push_back(ticket[1]);
            ticketsLeft[ticket[0] + "," + ticket[1]] += 1;
        }
        for (auto& pr : vertex) {
            sort(pr.second.begin(), pr.second.end());
        }
        
        unordered_set<string> vis;
        vector<string> ans;
        ans.push_back("JFK");
        dfs(vertex, ticketsLeft, ans, "JFK", tickets.size());
        
        return ans;
    }
};