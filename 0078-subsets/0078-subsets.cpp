class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> subres;
        int n = pow(2, nums.size()) - 1, tmp, ptr;
        for(int len = 0; len <= n; ++len) {
            tmp = len;
            ptr = 0;
            while(ptr < len) {
                if(tmp % 2) {
                    subres.push_back(nums[ptr]);
                }
                ++ptr;
                tmp = tmp / 2;
            }
            result.push_back(subres);
            subres.clear();
        }
        return result;
    }
};