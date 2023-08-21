class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        string s_ = s;
        char c;
        for(int i = 0; i < s.length() - 1; ++i) {
            c = s_[s_.length()-1];
            s_.pop_back();
            s_ = c + s_;
            if(s == s_) {
                return true;
            }
        }
        return false;
    }
};