/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        if (!root){
            return false;
        }

        int x = targetSum - root->val;
        if (x == 0){
            if (!root->left && !root->right){
                return true;
            }
        }
        // if (x < 0){
        //     return false;
        // }

        if (hasPathSum(root->left, x) || hasPathSum(root->right, x)){
            return true;
        }

        return false;
    }
};
