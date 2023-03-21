class Solution {
    private long numSubarrays(long n) {
        return (n * (n + 1)) / 2;
    }
    public long zeroFilledSubarray(int[] nums) {
        long res = 0, start_index = -1;
        boolean zero_seq = false;
        for(int i = 0; i < nums.length; ++i) {
            if(nums[i] == 0 && !zero_seq) {
                zero_seq = true;
                start_index = i;
            }
            else if(zero_seq && nums[i] != 0) {
                zero_seq= false;
                res += numSubarrays(i - start_index);
            }
        }
        if(zero_seq)
            res += numSubarrays(nums.length - start_index);
        return res;
    }
}