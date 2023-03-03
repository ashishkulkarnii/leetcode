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
    private int ans = 0;
    private int dfs(TreeNode root, int cs) {
        if(root != null) {
            cs = cs * 10 + root.val;
            dfs(root.left, cs);
            dfs(root.right, cs);
            if(root.left == null && root.right == null)
                ans += cs;
        }
        return cs;
    }
    public int sumNumbers(TreeNode root) {
        dfs(root, 0);
        return ans;
    }
}