class Solution {
public:
    bool isCircularSentence(string sentence) {
        if(sentence[0] != sentence[sentence.length()-1])
            return false;
        for(int i = 1; i < sentence.length() - 1; ++i)
            if(sentence[i] == ' ' and sentence[i-1] != sentence[i+1])
                return false;
        return true;
    }
};