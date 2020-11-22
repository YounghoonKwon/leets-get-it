// beat 58%. simple solution. O(n^2)
class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        vector<vector<int>> ans;
        sort(begin(people), end(people), [](const auto& l, const auto& r) {
            return l[0] == r[0] ? l[1] <= r[1] : l[0] > r[0];
        });
        
        for (auto person : people) {
            ans.insert(ans.begin() + person[1], person);
        }
        
        return ans;
    }
};

// beat 92.44%. using list. O(n^2)
class Solution1 {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        int n = people.size();
        sort(begin(people), end(people));
        vector<vector<int>> ans(n, {0, 0});
        list<vector<vector<int>>::iterator> l;
        for (auto it = begin(ans); it != end(ans); ++it) {
            l.push_back(it);
        }
        
        int height = -1;
        int dup = 0;
        for (auto& person : people) {
            if (height == person[0]) {
                dup += 1;
            }
            else {
                height = person[0];
                dup = 0;
            }
            
            int target = person[1] - dup;
            auto lit = next(l.begin(), target);
            **lit = person;
            l.erase(lit);
        }
        return ans;
    }
};

// beat 95.4% using fenwick tree. O(n * log(n)^2). Too complicated.
// better time complexity solution exists with using segment tree.
class Solution2 {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        int n = people.size();
        vector<vector<int>> ans(n, {-1, -1});
        
        int* f = new int[n + 1];
        for (int i = 1; i <= n; ++i) f[i] = i & -i;
        auto subf = [&](int i) { while (i <= n) f[i] -= 1, i += i & -i; };
        auto getf = [&](int i) { int sum = 0; while (i) sum += f[i], i -= i & -i; return sum;};
        
        sort(begin(people), end(people));
        int num = -1;
        int dup = 0;
        for (auto& person : people) {
            if (num == person[0]) {
                dup += 1;
            }
            else {
                num = person[0];
                dup = 0;
            }
            int l = 1;
            int h = n;
            int m = (l + h) / 2;
            int target = m;
            int wanted = person[1] + 1 - dup;
            while (l <= h) {
                //cout << "m : " << m << ", getf(m) : " << getf(m) << endl;
                int emptyCount = getf(m);
                if (emptyCount < wanted || 
                    (emptyCount == wanted && ans[m-1][0] == -1)) {
                    target = m;
                    l = m + 1;
                }
                else {
                    h = m - 1;
                }
                m = (l + h) / 2;
            }
            subf(target);
            //cout << target - 1<< endl;
            ans[target - 1] = person;
        }
        return ans;
    }
};