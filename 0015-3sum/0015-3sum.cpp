class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        int i = 0, j = 1, k = 2;
        if(nums[i] + nums[j] + nums[k] > 0) {
            return {};
        }
        while(i < nums.size() - 2) {
            if(i > 0 and nums[i] == nums[i-1]) {
                ++i;
                continue;
            }
            j = i + 1;
            k = nums.size() - 1;
            while(j < k) {
                if(nums[i] + nums[j] + nums[k] == 0) {
                    result.push_back({nums[i], nums[j], nums[k]});
                    while(nums[j] == nums[j + 1] and j < k - 1) {
                        ++j;
                    }
                    ++j;
                }
                else if(nums[i] + nums[j] + nums[k] < 0) {
                    ++j;
                }
                else {
                    --k;
                }
            }
            ++i;
        }
        return result;
    }
};