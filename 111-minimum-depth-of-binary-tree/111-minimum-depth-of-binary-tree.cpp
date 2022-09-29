/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 * };
 */
class Solution {
public:
    int minDepth(TreeNode* root) {
        if(root == NULL) {
            return 0;
        }
        if(root->left == NULL and root->right == NULL) {
            return 1;
        }
        else if(root->left == NULL) {
            return 1 + minDepth(root->right);
        }
        else if(root->right == NULL) {
            return 1 + minDepth(root->left);
        }
        else {
            return min(1 + minDepth(root->left), 1 + minDepth(root->right));
        }
    }
};