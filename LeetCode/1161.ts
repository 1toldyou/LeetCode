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

function maxLevelSum(root: TreeNode | null): number {
    let arr: number[] = [];
    work(root, 0, arr);

    let maxVal = Number.MIN_SAFE_INTEGER;
    let level = 0;
    for (let i = 0; i < arr.length; i++){
        if (arr[i] > maxVal){
            maxVal = arr[i];
            level = i;
        }
    }

    return level + 1;
};

function work(root: TreeNode | null, currentLevel: number, arr: number[]){
    if (!root){
        return;
    }

    if (arr[currentLevel] == undefined){  // 0 could trigger false 
        arr[currentLevel] = 0;
    }
    arr[currentLevel] += root.val;

    work(root.right, currentLevel+1, arr);
    work(root.left, currentLevel+1, arr);
}