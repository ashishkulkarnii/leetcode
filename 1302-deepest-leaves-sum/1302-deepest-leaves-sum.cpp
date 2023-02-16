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
    int depthTree(TreeNode* root, int depth) {
        if(!root) {
            return depth;
        }
        ++depth;
        return max(depthTree(root->left, depth), depthTree(root->right, depth));
    }
    int sumAtDepth(TreeNode* root, int curr_depth, int max_depth) {
        if(!root) {
            return 0;
        }
        ++curr_depth;
        if(curr_depth == max_depth) {
            return root->val;
        }
        else {
            return sumAtDepth(root->left, curr_depth, max_depth) + sumAtDepth(root->right, curr_depth, max_depth);
        }
    }
    int deepestLeavesSum(TreeNode* root) {
        return sumAtDepth(root, -1, depthTree(root, -1));
    }
};