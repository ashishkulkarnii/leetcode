class Solution {
    public int climbStairs(int n) {
        int first = 0, second = 1, temp;
        for(int i = 0; i < n; ++i) {
            temp = first;
            first = second;
            second += temp;
        }
        return second;
    }
}