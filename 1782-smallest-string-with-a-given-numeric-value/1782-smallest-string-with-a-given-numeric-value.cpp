class Solution {
public:
    string getSmallestString(int n, int k) {
        string res;
        res.append(n, 'a');
        k -= n; --n;
        while(k > 0) {
            if(k > 25) {
                res[n] = 'z';
                k -= 25;
                --n;
            }
            else {
                res[n] += k;
                break;
            }
        }
        return res;
    }
};