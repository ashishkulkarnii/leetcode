class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        vector<int> result;
        int c = 0;
        
        if(x <= arr[0]) {
            for(int i = 0; i < k; i++) {
                result.push_back(arr[i]);
            }
        }
        else if(x >= arr.back()) {
            for(int i = arr.size() - k; i < arr.size(); i++) {
                result.push_back(arr[i]);
            }
        }
        else {
            for(int i = 0; i < arr.size(); i++) {
                if(abs(arr[c] - x) > abs(arr[i] - x)) {
                    c = i;
                }
            }
            for(int i = c - k > 0 ? c - k + 1 : 0; i < arr.size() and i < c + k; i++) {
                result.push_back(arr[i] - x);
            }
            int i = 0;
            while(result.size() > k) {
                if(abs(result[0]) > abs(result.back())) {
                    result.erase(result.begin(), result.begin() + 1);
                }
                else {
                    result.pop_back();
                }
                i++;
            }
            for(int i = 0; i < result.size(); i++) {
                result[i] += x;
            }
        }
        
        return result;
    }
};