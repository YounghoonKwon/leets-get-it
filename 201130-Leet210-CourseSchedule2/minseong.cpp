// beat 99.52% TC. 84.28% SC.
// using topological sort
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> fromTo(numCourses);
        vector<int> ind(numCourses);
        for (auto& pre : prerequisites) {
            ind[pre[0]] += 1;
            fromTo[pre[1]].push_back(pre[0]);
        }
        
        vector<int> ans;
        queue<int> q;
        for (int i = 0; i < numCourses; ++i) {
            if (ind[i] == 0) {
                q.push(i);
                ans.push_back(i);
            }
        }
        
        while (q.size()) {
            int from = q.front();
            q.pop();
            
            for (int to : fromTo[from]) {
                ind[to] -= 1;
                if (ind[to] == 0) {
                    q.push(to);
                    ans.push_back(to);
                }
            }
        }
        
        return ans.size() == numCourses ? ans : vector<int>();
    }
};

static const auto speedUpIO = []() {
    ios::sync_with_stdio(false);
    return 1;
}();