class Solution {
    public int search(int[] nums, int target) {
        int b = 0, e = nums.length - 1, m;
        while(b <= e) {
            m = b + (e - b) / 2;
            if(nums[m] == target) {
                return m;
            }
            else if(nums[m] > target) {
                e = m - 1;
            }
            else {
                b = m + 1;
            }
        }
        return target == nums[0] ? 0 : -1;
    }
}