class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> n_i;
        for(int i = 0; i < nums.size(); ++i) {
            if(n_i.find(target - nums[i]) != n_i.end()) {
                return {i, n_i[target-nums[i]]};
            }
            n_i[nums[i]] = i;
        }
        return {};
    }
};