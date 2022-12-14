class Solution {
public:
    bool isPerfectSquare(int x) {
        long long int beg = 0, end = x, mid = x / 2;
        while(beg <= end) {
            if(mid * mid > x) {
                end = mid - 1;
            }
            else if(mid * mid < x) {
                beg = mid + 1;
            }
            else {
                break;
            }
            mid = (beg + end) / 2;
        }
        return mid * mid == x;
    }
};