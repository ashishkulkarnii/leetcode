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
import java.lang.Math;

class Solution {
    private int min_depth = Integer.MAX_VALUE, max_depth = 0;
    private boolean valid = true;
    private void findDepths(TreeNode node, int depth) {
        System.out.println(min_depth + " " + max_depth + " " + depth);
        if(node == null) {
            if(depth > min_depth)
                valid = false;
            min_depth = Math.min(min_depth, depth);
            max_depth = Math.max(max_depth, depth);
        }
        else {
            findDepths(node.left, depth + 1);
            findDepths(node.right, depth + 1);
        }
    }
    public boolean isCompleteTree(TreeNode root) {
        findDepths(root, 0);
        if(max_depth - min_depth > 1)
            valid = false;
        return valid;
    }
}