class Solution {
public:
    bool isIn(vector<int> arr, int n) {
        for(int i = 0; i < arr.size(); i++) {
            if(arr[i] == n) {
                return true;
            }
        }
        return false;
    }
    int count(vector<int> arr, int n) {
        int c = 0;
        for(int i = 0; i < arr.size(); i++) {
            if(arr[i] == n) {
                c++;
            }
        }
        return c;
    }
    vector<int> majorityElement(vector<int>& nums) {
        vector<int> checked, result;
        int temp;
        for(int i = 0; i < nums.size(); i++) {
            if(not isIn(checked, nums[i])) {
                checked.push_back(nums[i]);
                temp = count(nums, nums[i]);
                if(temp > (float) nums.size() / 3) {
                    result.push_back(nums[i]);
                }
            }
        }
        return result;
    }
};