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
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return recur(nums, 0, nums.size()-1);
    }

    TreeNode* recur(vector<int>& nums, int a, int b){
        if (a == b){
            return new TreeNode(nums[a]);
        }

        if (b-a <= 2){
            return new TreeNode(
                nums[a+1], 
                new TreeNode(nums[a]),
                b-a == 2 ? new TreeNode(nums[b]) : nullptr
            );
        }

        int mid = (b - a) / 2 + a;
        return new TreeNode(
            nums[mid],
            recur(nums, a, mid-1),
            recur(nums, mid+1, b)
        );
    }
};
