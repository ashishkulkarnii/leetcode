class Solution {
public:
    int tribonacci(int n) {
        int t0 = 0, t1 = 1, t2 = 1, t3;
        switch(n) {
            case 0:
                return t0;
            case 1:
                return t1;
            case 2:
                return t2;
        }
        for(int i = 3; i <= n; i++) {
            t3 = t2 + t1 + t0;
            t0 = t1;
            t1 = t2;
            t2 = t3;
        }
        return t3;
    }
};