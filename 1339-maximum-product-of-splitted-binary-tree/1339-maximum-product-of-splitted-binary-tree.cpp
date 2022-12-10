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
    int modulo = 1e9 + 7;
    long long totalSum(TreeNode* node) {
        if(node == NULL) {
            return 0;
        }
        return totalSum(node->left) + totalSum(node->right) + node->val;
    }
    long long getRes(TreeNode* node, long long total, long long &res) {
        if(node == NULL) {
            return 0;
        }
        long long sum_subtree = 0;
        sum_subtree += getRes(node->left, total, res);
        sum_subtree += getRes(node->right, total, res);
        sum_subtree += node->val;
        res = max(res, sum_subtree * (total - sum_subtree));
        return sum_subtree;
    }
    int maxProduct(TreeNode* root) {
        long long total = totalSum(root), res = 0;
        getRes(root, total, res);
        return res % modulo;
    }
};