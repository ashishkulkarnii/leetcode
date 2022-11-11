class Solution {
public:
    int lengthOfLastWord(string s) {
        int res = 0, i = s.size() - 1;
        while(i >= 0 and s[i] == ' ') {
            --i;
        }
        while(i >= 0 and s[i] != ' ') {
            --i;
            ++res;
        }
        return res;
    }
};