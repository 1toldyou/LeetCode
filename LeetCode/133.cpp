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

class Solution {
    Node* nodes[101] = {};
    bool processed[101];

    void recur(Node* node){
        int key = node->val;
        if (processed[key] == true){
            return;
        }
    
        if (nodes[key] == nullptr){
            nodes[key] = new Node(key);
        }
        
        for (Node* neighbor : node->neighbors){
            int neighborKey = neighbor->val;
            if (nodes[neighborKey] == nullptr){
                nodes[neighborKey] = new Node(neighborKey);
            }
            nodes[key]->neighbors.push_back(nodes[neighborKey]);
        }
        processed[key] = true;

        for (Node* neighbor : node->neighbors){
            int neighborKey = neighbor->val;
            recur(neighbor);
        }
    }
public:
    Node* cloneGraph(Node* node) {
        if (!node){
            return nullptr;
        }

        recur(node);
        return nodes[node->val];
    }
};
