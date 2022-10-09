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
    void store(TreeNode* root, vector<int> &arr) {
        if(root == NULL) {
            return;
        }
        store(root->left, arr);
        arr.push_back(root->val);
        store(root->right, arr);
    }
    bool findTarget(TreeNode* root, int k) {
        vector<int> nums;
        store(root, nums);
        for(int i = 0; i < nums.size() - 1; i++) {
            for(int j = i + 1; j < nums.size(); j++) {
                if(nums[i] + nums[j] == k) {
                    return 1;
                }
            }
        }
        return 0;
        
    }
};