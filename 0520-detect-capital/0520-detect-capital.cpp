class Solution {
public:
    bool detectCapitalUse(string word) {
        if(word.length() <= 1)
            return true;
        bool all_upper = false;
        if(word[0] >= 'A' and word[0] <= 'Z') {
            if(word[1] >= 'A' and word[1] <= 'Z')
                all_upper = true;
        }
        for(int i = 1; i < word.length(); ++i) {
            if(all_upper) {
                if(word[i] < 'A' or word[i] > 'Z')
                    return false;
            }
            else
                if(word[i] < 'a' or word[i] > 'z')
                    return false;
        }
        return true;
    }
};