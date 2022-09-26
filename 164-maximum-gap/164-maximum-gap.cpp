class Solution {
public:
    int maximumGap(vector<int>& nums) {
        int res = 0;
        sort(nums.begin(), nums.end());
        for(int i = 0; i < nums.size() - 1; i++) {
            if(abs(nums[i] - nums[i+1]) > res) {
                res = abs(nums[i] - nums[i+1]);
            }
        }
        return res;
    }
};