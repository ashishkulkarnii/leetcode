class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        vector<int> temp;
        int i;
        for(i = 0; i < nums.size(); i++) {
            if(nums[i] != val) {
                temp.push_back(nums[i]);
            }
        }
        for(i = 0; i < temp.size(); i++) {
            nums[i] = temp[i];
        }
        return temp.size();
    }
};