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
    bool comp(int a, int b) {
        return a < b;
    }
    int diff(TreeNode* root, int max_val, int min_val) {
        if(root == NULL) {
            return max_val - min_val;
        }
        max_val = max(max_val, root->val);
        min_val = min(min_val, root->val);
        return max(diff(root->left, max_val, min_val), diff(root->right, max_val, min_val));
    }
    int maxAncestorDiff(TreeNode* root) {
        return diff(root, root->val, root->val);
    }
};