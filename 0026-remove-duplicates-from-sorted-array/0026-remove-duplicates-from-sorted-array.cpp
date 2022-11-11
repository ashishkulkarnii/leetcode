class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i = 0;
        vector<int> temp;
        temp.push_back(nums[0]);
        while( i < nums.size() - 1) {
            if(nums[i] == nums[i + 1]) {
                i++;
            }
            else {
                temp.push_back(nums[i + 1]);
                i++;
            }
        }
        for(int i = 0; i < temp.size(); i++) {
            nums[i] = temp[i];
        }
        return temp.size();
    }
};