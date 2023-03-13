class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int len = nums.size();
        int beg = 0, end = len - 1;
        int mid = (beg + end) / 2;
        while(end > beg) {
            if(nums[mid] == target) {
                return mid;
            }
            else if(nums[mid] > target) {
                end = mid - 1;
            }
            else {
                beg = mid + 1;
            }
            mid = (beg + end) / 2;
        }
        if(target > nums[mid])
            return ++mid;
        else
            return mid;
    }
};