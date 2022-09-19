class Solution {
public:
    bool isPowerOfFour(int n) {
        if(n == 1) {
            return true;
        }
        while(n > 4) {
            if(n % 4 == 0) {
                n = n / 4;
            }
            else {
                return false;
            }
        }
        return n == 4;
    }
};