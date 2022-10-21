class Solution {
public:
    int totalHammingDistance(vector<int>& nums) {
        int res = 0;
        int z, o;
        for(int i = 0; i < 32; ++i) {
            z = 0;
            o = 0;
            for(int n = 0; n < nums.size(); ++n) {
                if((nums[n] >> i) & 1) {
                    ++o;
                }
                else {
                    ++z;
                }
            }
            res += z * o;
        }
        return res;
    }
};