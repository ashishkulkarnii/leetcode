class Solution {
public:
    bool isSubsequence(string s, string t) {
        int sub = 0;
        for(int i = 0; i < t.size(); i++) {
            if(s[sub] == t[i]) {
                sub++;
            }
        }
        return sub == s.length();
    }
};