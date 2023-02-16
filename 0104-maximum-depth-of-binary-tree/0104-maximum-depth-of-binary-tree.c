/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

#define max(a,b) \
    ({ __typeof__ (a) _a = (a); \
       __typeof__ (b) _b = (b); \
       _a > _b ? _a : _b; })

int maxDepth1(struct TreeNode* root, int depth){
    if(root == NULL) {
        return depth;
    } else {
        ++depth;
        return max(maxDepth1(root->left, depth), maxDepth1(root->right, depth));
    }
}

int maxDepth(struct TreeNode* root) {
    return maxDepth1(root, 0);
}