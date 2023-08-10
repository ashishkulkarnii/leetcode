class Solution {
    public boolean search(int[] nums, int target) {
        // finding pivot
        int n = nums.length, start = 0;
        for(int i = 1; i < n; ++i) {
            if(nums[i-1] > nums[i]) {
                start = i - 1;
                if(nums[i-1] == target || nums[i] == target)
                    return true;
                break;
            }
            if(target == nums[i-1])
                return true;
        }
        // finding target
        int temp, low = 0, high = n - 1, mid;
        while(low <= high) {
            mid = (high + low) / 2;
            temp = (start + mid) % n;
            if(nums[temp] == target)
                return true;
            else if(nums[temp] < target)
                low = mid + 1;
            else
                high = mid - 1;
        }
        return false;
    }
}