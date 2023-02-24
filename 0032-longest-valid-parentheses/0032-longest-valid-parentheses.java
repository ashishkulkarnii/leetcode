import java.util.*;
import java.lang.*;

class Solution {
    public int longestValidParentheses(String s) {
        char[] string = s.toCharArray();
        Stack<Character> stack = new Stack<Character>();
        int res = 0, left = 0, right = 0;
        for(char c: string) {
            if(c == '(')
                ++left;
            else
                ++right;
            if(left == right) {
                res = Math.max(res, left + right);
            }
            else if(right >= left) {
                left = right = 0;
            }
        }
        left = right = 0;
        char c;
        for(int i = string.length - 1; i >= 0; --i) {
            c = string[i];
            if(c == '(')
                ++left;
            else
                ++right;
            if(left == right) {
                res = Math.max(res, left + right);
            }
            else if(left >= right) {
                left = right = 0;
            }
        }
        return res;
    }
}