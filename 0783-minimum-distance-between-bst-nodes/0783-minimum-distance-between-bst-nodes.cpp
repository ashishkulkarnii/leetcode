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
    vector<int> inorder;
    void inorderTraversal(TreeNode* root) {
        if(root == NULL)
            return ;
        inorderTraversal(root->left);
        inorder.push_back(root->val);
        inorderTraversal(root->right);
    }
    int minDiffInBST(TreeNode* root) {
        inorderTraversal(root);
        int res = INT_MAX;
        for(int i = 1; i < inorder.size(); ++i) {
            res = min(res, abs(inorder[i] - inorder[i-1]));
        }
        return res;
    }
};