class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int i = 0;
        while(i < nums.size()) {
            if(i != nums.size() - 1 and nums[i] == nums[i+1]) {
                i += 2;
            }
            else {
                return nums[i];
            }
        }
        return nums[i];
    }
};