class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        int len = nums.size();
        if(len == 1)
            return true;
        bool asc;
        int st;
        for(int i = 0; i < len - 1; ++i) {
            if(nums[i] < nums[i+1]) {
                asc = true;
                st = i + 1;
                break;
            }
            if(nums[i] > nums[i+1]) {
                asc = false;
                st = i + 1;
                break;
            }
            if(nums[i] == nums[i+1] && i + 1 == len - 1)
                return true;
        }
        if(asc == true) {
            for(int i = st; i < len - 1; ++i)
                if(nums[i] > nums[i+1])
                    return false;
            return true;
        }
        else {
            for(int i = st; i < len - 1; ++i)
                if(nums[i] < nums[i+1])
                    return false;
            return true;
        }
    }
};