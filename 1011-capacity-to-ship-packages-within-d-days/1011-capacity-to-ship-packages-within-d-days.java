import java.util.Arrays;

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
        int b = Arrays.stream(weights).max().getAsInt(), e = Arrays.stream(weights).sum(), m;
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