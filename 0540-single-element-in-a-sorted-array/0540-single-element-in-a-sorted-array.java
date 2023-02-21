class Solution {
    public int singleNonDuplicate(int[] nums) {
        int b = 0, e = nums.length - 1, m = 0;
        while(b < e) {
            m = (b + e) / 2;
            if(m % 2 == 0 && nums[m] == nums[m+1] || m % 2 == 1 && nums[m] == nums[m-1]) {
                b = m + 1;
            }
            else {
                e = m;
            }
        }
        return nums[b];
    }
}