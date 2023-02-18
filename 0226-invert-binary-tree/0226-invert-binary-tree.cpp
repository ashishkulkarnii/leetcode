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
    TreeNode* res = new TreeNode();
    void invert(TreeNode* root, TreeNode* res) {
        if(root == NULL)
            return;
        res->val = root->val;
        if(root->right) {
            res->left = new TreeNode();
            invert(root->right, res->left);
        }
        if(root->left) {
            res->right = new TreeNode();
            invert(root->left, res->right);
        }
    }
    TreeNode* invertTree(TreeNode* root) {
        if(root == nullptr)
            return nullptr;
        invert(root, res);
        return res;
    }
};