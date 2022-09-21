class Solution {
public:
    int evenSum(vector<int>& nums) {
        int sum = 0;
        for(int i = 0; i < nums.size(); i++) {
            if(nums[i] % 2 == 0) {
                sum += nums[i];
            }
        }
        return sum;
    }
    vector<int> sumEvenAfterQueries(vector<int>& nums, vector<vector<int>>& queries) {
        vector<int> result;
        int temp_index, temp_val, totalevensum = evenSum(nums);
        for(int i = 0; i < queries.size(); i++) {
            temp_index = queries[i][1];
            temp_val = queries[i][0];
            if(nums[temp_index] % 2 == 0 and temp_val % 2 == 0) {
                totalevensum += temp_val;
            }
            else if(nums[temp_index] % 2 == 0 and temp_val % 2 != 0) {
                totalevensum = totalevensum - nums[temp_index]; 
            }
            else if(nums[temp_index] % 2 != 0 and temp_val % 2 != 0) {
                totalevensum += temp_val + nums[temp_index];
            }
            nums[temp_index] += temp_val;
            result.push_back(totalevensum);
        }
        return result;
    }
};
