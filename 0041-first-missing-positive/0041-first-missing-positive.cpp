// O(n logn) time

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int res = 1;
        for(auto n: nums) {
            if(res == n) {
                res += 1;
            }
        }
        return res;
    }
};