class Solution {
public:
    int countAsterisks(string s) {
        bool ignore = false;
        int count = 0;
        for(int i = 0; i < s.length(); i++){
            switch(s[i]){
                case '|':
                    ignore = not ignore;
                    break;
                case '*':
                    if(not ignore){
                        count++;
                    }
                    break;
            }
        }
        return count;
    }
};