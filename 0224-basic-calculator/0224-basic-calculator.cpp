class Solution {
public:
    int calculate(string s) {
        stack<int> nums;
        stack<int> ops;
        
        int n = 0, sign = 1, ans = 0;
        
        for(char c: s) {
            if(c >= '0' and c <= '9') {
                n = n * 10 + ((int) c - '0');
            }
            else {
                ans += n * sign;
                n = 0;
                switch(c) {
                    case '+':
                        sign = 1;
                        break;
                    case '-':
                        sign = -1;
                        break;
                    case '(':
                        nums.push(ans);
                        ops.push(sign);
                        ans = 0;
                        sign = 1;
                        break;
                    case ')':
                        ans = ops.top() * ans + nums.top();
                        ops.pop(); nums.pop();
                        n = 0;
                        break;
                }
            }
        }
        return ans + sign * n;
    }
};