class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if(s2.length() < s1.length())
            return false;
        
        array<int, 26> slider = {0}, letters = {0};
        
        for(int i = 0; i < s1.length(); ++i) {
            ++letters[s1[i] - 'a'];
            ++slider[s2[i] - 'a'];
        }
        if(slider == letters)
            return true;
        
        for(int i = 1; i <= s2.length() - s1.length(); ++i) {
            --slider[s2[i-1] - 'a'];
            ++slider[s2[i+s1.length()-1] - 'a'];
            if(slider == letters)
                return true;
        }
        
        return false;
    }
};