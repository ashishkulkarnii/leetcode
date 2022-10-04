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
    bool hasPathSum(TreeNode* root, int targetSum, int pathSum = 0) {
        if(root == NULL) {
            return false;
        }
        pathSum += root->val;
        if(root->right == NULL and root->left == NULL) {
            return pathSum == targetSum;
        }
        else if(root->right == NULL) {
            return hasPathSum(root->left, targetSum, pathSum);
        }
        else if(root->left == NULL) {
            return hasPathSum(root->right, targetSum, pathSum);
        }
        else {
            return hasPathSum(root->right, targetSum, pathSum) or hasPathSum(root->left, targetSum, pathSum);
        }
    }
};