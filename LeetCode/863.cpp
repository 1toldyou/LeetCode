/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
    vector<int> result;
    TreeNode* parent[1001] = {};
    bool visited[1001] = {};

    void recordParent(TreeNode* root){
        if (!root){
            return;
        }

        if (root->left){
            parent[root->left->val] = root;
            recordParent(root->left);
        }
        if (root->right){
            parent[root->right->val] = root;
            recordParent(root->right);
        }
    }

    void visit(TreeNode* root, int dist){
        if (!root){
            return;
        }
        
        int val = root->val;
        if (visited[val]){
            return;
        }

        visited[val] = true;

        if (dist == 0){
            result.push_back(val);
        }

        visit(root->left, dist-1);
        visit(root->right, dist-1);
        visit(parent[val], dist-1);
    }

public:
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        recordParent(root);

        visit(target, k);

        return result;
    }
};
