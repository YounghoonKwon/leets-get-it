/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

// beat 99.85% TC
// beat 83.33% SC
class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (node == nullptr) {
            return nullptr;
        }
        Node* valToNode[101];
        for (int i = 1; i <= 100; ++i) {
            valToNode[i] = new Node(i);
        }
        
        unordered_set<Node*> vis;
        queue<Node*> q;
        q.push(node);
        vis.insert(node);
        while (q.size()) {
            Node* curNode = q.front();
            int curValue = curNode->val;
            q.pop();
            for (auto& next : curNode->neighbors) {
                valToNode[curValue]->neighbors.push_back(valToNode[next->val]);
                if (vis.find(next) == vis.end()) {
                    vis.insert(next);
                    q.push(next);
                }
            }
        }
        
        return valToNode[node->val];
    }
};

static const auto speedUpIO = []() {
    ios::sync_with_stdio(false);
    return 1;
}();