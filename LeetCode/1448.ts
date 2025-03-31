/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function goodNodes(root: TreeNode | null): number {
    if (!root){
        return 0;
    }

    return 1 + work(root.left, root.val) + work(root.right, root.val);
};

function work(root: TreeNode | null, biggestInPath: number): number {
    if (!root){
        return 0;
    }

    return ((biggestInPath <= root.val) ? 1 : 0 ) 
        + work(root.left, Math.max(biggestInPath, root.val)) 
        + work(root.right, Math.max(biggestInPath, root.val));
}