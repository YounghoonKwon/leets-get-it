// beat 95.21% TC. 87.11% SC.
// using topological sort
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> fromTo(numCourses);
        vector<int> ind(numCourses);
        for (auto& pre : prerequisites) {
            ind[pre[0]] += 1;
            fromTo[pre[1]].push_back(pre[0]);
        }
        
        int count = 0;
        queue<int> q;
        for (int i = 0; i < numCourses; ++i) {
            if (ind[i] == 0) {
                q.push(i);
                ++count;
            }
        }
        
        while (q.size()) {
            int from = q.front();
            q.pop();
            
            for (int to : fromTo[from]) {
                ind[to] -= 1;
                if (ind[to] == 0) {
                    q.push(to);
                    ++count;
                }
            }
        }
        
        return count == numCourses;
    }
};

static const auto speedUpIO = []() {
    ios::sync_with_stdio(false);
    return 1;
}();