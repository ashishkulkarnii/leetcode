class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        string w1 = "", w2 = "";
        for(auto s: word1) {
            w1 += s;
        }
        for(auto s: word2) {
            w2 += s;
        }
        if(w1.length() == w2.length()) {
            for(int i = 0; i < w1.length(); i++) {
                if(w1[i] != w2[i]) {
                    return false;
                }
            }
            return true;
        }
        return false;
    }
};