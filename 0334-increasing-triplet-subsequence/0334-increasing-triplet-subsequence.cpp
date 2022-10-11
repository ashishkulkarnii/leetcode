class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int j = INT_MAX, k = INT_MAX;
        for(int i = 0; i < nums.size(); ++i) {
            if(nums[i] < j) {
                j = nums[i];
            }
            else if(nums[i] < k and nums[i] > j) {
                k = nums[i];
            }
            else {
                if(k < nums[i]) {
                    return true;
                }
            }
        }
        return false;
    }
};