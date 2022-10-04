class Solution {
public:
    int brokenCalc(int n, int target) {
        int res = 0;
        while(target != n) {
            if(target > n) {
                if(target % 2 == 1) {
                    target++;
                    res++;
                }
                target /= 2;
                res++;
            }
            else {
                target++;
                res++;
            }
        }
        return res;
    }
};