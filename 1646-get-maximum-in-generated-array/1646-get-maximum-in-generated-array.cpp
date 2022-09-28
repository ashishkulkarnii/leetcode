class Solution {
public:
    int getMaximumGenerated(int n) {
        if(n < 2) {
            return n;
        }
        vector<int> nums;
        nums.push_back(0);
        nums.push_back(1);
        int max = 1;
        for(int i = 2; i <= n; i++) {
            if(i % 2 == 0) {
                nums.push_back(nums[i/2]);
                max = nums[i/2] > max ? nums[i/2] : max;
            }
            else {
                nums.push_back(nums[(i-1)/2] + nums[(i+1)/2]);
                max = nums[(i-1)/2] + nums[(i+1)/2] > max ? nums[(i-1)/2] + nums[(i+1)/2] : max;
            }
        }
        return max;
    }
};