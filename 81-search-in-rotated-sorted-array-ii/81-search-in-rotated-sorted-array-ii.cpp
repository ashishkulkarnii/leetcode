class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int pivot = 0;
        if(nums[0] == target) {
            return true;
        }
        int i = 1;
        for(i = 1; i < nums.size(); i++) {
            if(nums[i] == target) {
                return true;
            }
            if(nums[i-1] > nums[i]) {
                pivot = i;
                break;
            }
        }
        if(i == nums.size() - 1) {
            return false;
        }
        int b = pivot, e = nums.size() - 1;
        while(b <= e) {
            i = (b + e) / 2;
            if(nums[i] == target) {
                return true;
            }
            else if(nums[i] < target) {
                b = i + 1;
            }
            else {
                e = i - 1;
            }
        }
        return false;
    }
};