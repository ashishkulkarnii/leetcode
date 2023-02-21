class Solution {
    public int firstMissingPositive(int[] nums) {
        int n = nums.length, temp;
        for(int i = 0; i < n; ++i) {
            while(nums[i] > 0 && nums[i] <= n && nums[nums[i]-1] != nums[i]) {
                temp = nums[i] - 1;
                nums[i] = nums[i] ^ nums[temp];
                nums[temp] = nums[i] ^ nums[temp];
                nums[i] = nums[i] ^ nums[temp];
            }
        }
        for(int i = 0; i < n; ++i) {
            if(nums[i] - 1 != i) {
                return i + 1;
            }
        }
        return n + 1;
    }
}