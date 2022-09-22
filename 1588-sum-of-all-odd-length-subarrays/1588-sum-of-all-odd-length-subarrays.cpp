class Solution {
public:
    int sumOddLengthSubarrays(vector<int>& arr) {
        int res = 0;
        for(int len = 1; len <= arr.size(); len += 2) {
            for(int i = 0; i <= arr.size() - len; i++) {
                for(int j = i; j < i + len; j++) {
                    res += arr[j];
                }
            }
        }
        return res;
    }
};