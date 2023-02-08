class Solution {
    public int jump(int[] nums) {
        int res = 0, left = 0, right = 0, max_jump;
        while(right < nums.length - 1) {
            max_jump = 0;
            for(int i = left; i <= right; ++i)
                max_jump = Math.max(max_jump, i + nums[i]);
            left = right + 1;
            right = max_jump;
            ++res;
        }
        return res;
    }
}