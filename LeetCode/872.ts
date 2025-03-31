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

function leafSimilar(root1: TreeNode | null, root2: TreeNode | null): boolean {
    if (!root1 && !root2){
        return true;
    }
    else if (!(root1 && root2)){
        return false;
    }

    // console.log("root1", root1);
    // console.log("root2", root2);
    let leftLeafs = getLeafValues(root1);
    let rightLeafs = getLeafValues(root2);
    // console.log("leftLeafs", leftLeafs);
    // console.log("rightLeafs", rightLeafs);

    if (leftLeafs.length != rightLeafs.length){
        return false;
    }
    for (let i = 0; i < leftLeafs.length; i++){
        if (leftLeafs[i] != rightLeafs[i]){
            return false;
        }
    }
    return true;
};

function getLeafValues(tree: TreeNode): number[] {
    if (!tree){
        return [];
    }
    if (isLeafNode(tree)){
        return [tree.val];
    }


    // return [
    //     isLeafNode(tree.left) ? tree.left.val : (...getLeafValues(tree.left)),
    //     isLeafNode(tree.left) ? tree.right.val : (...getLeafValues(tree.right)),
    // ]

    return [
        ...isLeafNode(tree.left) ? [tree.left.val] : getLeafValues(tree.left),
        ...isLeafNode(tree.right) ? [tree.right.val] : getLeafValues(tree.right)
    ];
}

function isLeafNode(tree: TreeNode): boolean {
    if (!tree){
        // throw new Error("isLeafNode(): tree is empty");
        return false;
    }
    return tree.left == null && tree.right == null;
}