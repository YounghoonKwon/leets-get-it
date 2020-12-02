class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        vector<bool> vis(rooms.size());
        queue<int> q;
        int cnt = 1;
        vis[0] = true;
        q.push(0);
        while (q.size()) {
            int cur = q.front(); q.pop();
            for (int to : rooms[cur]) {
                if (vis[to] == false) {
                    vis[to] = true;
                    q.push(to);
                    ++cnt;
                }
            }
        }
        
        return cnt == rooms.size() ? true : false;
    }
};