/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {  
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if(root == null){
            return root == subRoot;
        }

        return sameTree(root, subRoot) || isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
    }

    public boolean sameTree(TreeNode currNode, TreeNode currSubNode){
        if(currSubNode == null && currNode == null){
            return true;
        } else if(currNode == null || currSubNode == null){
            return false;
        }

        return currNode.val == currSubNode.val && sameTree(currNode.left, currSubNode.left) && sameTree(currNode.right, currSubNode.right);
    }
}
