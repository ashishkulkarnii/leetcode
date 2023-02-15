class Solution {
public:
    vector<int> addToArrayForm(vector<int>& num, int k) {
        int temp;
        for(int i = num.size() - 1; i >= 0; --i) {
            num[i] += k;
            temp = num[i] % 10;
            k = (num[i] - temp) / 10;
            num[i] = temp;
        }
        if(k != 0) {
            reverse(num.begin(), num.end());
            while(k != 0) {
                num.push_back(k % 10);
                k -= k % 10;
                k /= 10;
            }
            reverse(num.begin(), num.end());
        }
        return num;
    }
};