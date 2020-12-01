class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int N, int K) {
        vector<vector<pair<int, int>>> edges(N + 1);
        for (auto& time : times) {
            edges[time[0]].push_back({time[1], time[2]});
        }
        
        int inf = 1e9;
        vector<int> dist(N + 1, inf);
        priority_queue<pair<int, int>, vector<pair<int, int>>, less<pair<int, int>>> pq;
        dist[0] = dist[K] = 0;
        pq.push({0, K});
        while (pq.size()) {
            int cur = pq.top().second;
            pq.pop();
            
            for (auto& to : edges[cur]) {
                int nextCost = dist[cur] + to.second;
                if (nextCost < dist[to.first]) {
                    dist[to.first] = nextCost;
                    pq.push({nextCost, to.first});
                }
            }
        }
        
        int ans = *max_element(begin(dist), end(dist));
        return ans == inf ? -1 : ans;
    }
};
