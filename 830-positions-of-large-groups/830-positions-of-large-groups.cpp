class Solution {
public:
    vector<vector<int>> largeGroupPositions(string s) {
        int beg = 0, end = 0;
        vector<vector<int>> result;
        while(end < s.length()) {
            if(s[beg] = s[end]) {
                end++;
            }
            if(s[beg] != s[end]) {
                if(end - beg >= 3) {
                    result.push_back({beg, end - 1});
                }
                beg = end;
            }
        }
        return result;
    }
};