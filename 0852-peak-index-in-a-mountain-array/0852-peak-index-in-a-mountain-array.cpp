class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        int res = 0;
        for(int i = 1; i < arr.size() - 1; ++i) {
            if(arr[res] < arr[i] and arr[i] > arr[i-1]) {
                if(i != arr.size() - 1) {
                    if(arr[i] > arr[i+1]) {
                        res = i;
                    }
                }
                else {
                    res = i;
                }
            }
        }
        return res;
    }
};