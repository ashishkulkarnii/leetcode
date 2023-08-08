class Solution {
    public int search(int[] nums, int target) {
        // finding pivot
        int n = nums.length, low = 0, high = n - 1, mid = (n - 1) / 2;
        if(nums[low] < nums[high])
            mid = -1;
        else
            while(low < high) {
                mid = (high + low) / 2;
                if(nums[mid] > nums[low])
                    low = mid;
                else
                    high = mid;
            }
        int start = mid + 1;
        // finding target
        int temp; low = 0; high = n - 1;
        while(low <= high) {
            mid = (high + low) / 2;
            temp = (start + mid) % n;
            if(nums[temp] == target)
                return temp;
            else if(nums[temp] < target)
                low = mid + 1;
            else
                high = mid - 1;
        }
        return -1;
    }
}