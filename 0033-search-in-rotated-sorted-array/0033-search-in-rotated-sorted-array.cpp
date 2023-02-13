class Solution {
public:
    int map(int index, int start, int arr_size) {
        return index + start - (index + start < arr_size ? 0 : arr_size);
    }
    int search(vector<int>& nums, int target) {
        int start = 0;
        for(int i = 1; i < nums.size(); ++i) {
            if(nums[i] < nums[i-1]) {
                start = i;
                break;
            }
        }
        // binary search
        int high = nums.size() - 1, low = 0, mid;
        while(high >= low) {
            mid = (high + low) / 2;
            if(nums[map(mid, start, nums.size())] == target) {
                return map(mid, start, nums.size());
            }
            else if(nums[map(mid, start, nums.size())] > target) {
                high = mid - 1;
            }
            else {
                low = mid + 1;
            }
        }
        return -1;
    }
};