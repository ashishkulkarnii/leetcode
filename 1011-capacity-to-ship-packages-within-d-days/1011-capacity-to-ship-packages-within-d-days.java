import java.util.Arrays;
import java.lang.Math;

class Solution {
    public boolean valid(int[] weights, int capacity, int days) {
        int running_sum = 0, res = 1;
        for(int w: weights) {
            running_sum += w;
            if(running_sum > capacity) {
                running_sum = w;
                ++res;
            }
        }
        return res <= days;
    }
    public int shipWithinDays(int[] weights, int days) {
        int b = Integer.MIN_VALUE, e = 0, m;
        for(int w: weights) {
            b = Math.max(b, w);
            e += w;
        }
        while(b < e) {
            m = (b + e) / 2;
            if(valid(weights, m, days)) {
                e = m;
            }
            else {
                b = m + 1;
            }
        }
        return b;
    }
}