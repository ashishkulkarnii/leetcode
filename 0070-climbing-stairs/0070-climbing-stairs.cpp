class Solution {
public:
    int climbStairs(int n) {
        int first = 0, second = 1, result = 0, steps = 0;
        while(steps < n) {
            result = first + second;
            first = second;
            second = result;
            steps++;
        }
        return result;
    }
};