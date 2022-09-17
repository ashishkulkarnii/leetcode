class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int start = -1, end = -1;
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] > target and start == -1){
                break;
            }
            if(nums[i] == target and start == -1){
                start = i;
            }
            if(start != -1 and nums[i] > target){
                end = i-1;
                break;
            }
        }
        if(start != -1 and end == -1){
            end = nums.size() - 1;
        }
        return {start, end};
    }
};