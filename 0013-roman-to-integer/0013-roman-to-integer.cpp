class Solution {
public:
    int romanToInt(string s) {
        int res = 0;
        for(int i = 0; i < s.length(); ++i) {
            switch(s[i]) {
                case 'I':
                    if(i + 1 == s.length()) {
                        res += 1;
                    }
                    else {
                        if(s[i+1] == 'V' or s[i+1] == 'X') {
                            res += -1;
                        }
                        else {
                            res += 1;
                        }
                    }
                    break;
                case 'V':
                    res += 5;
                    break;
                case 'X':
                    if(i + 1 == s.length()) {
                        res += 10;
                    }
                    else {
                        if(s[i+1] == 'L' or s[i+1] == 'C') {
                            res += -10;
                        }
                        else {
                            res += 10;
                        }
                    }
                    break;
                case 'L':
                    res += 50;
                    break;
                case 'C':
                    if(i + 1 == s.length()) {
                        res += 100;
                    }
                    else {
                        if(s[i+1] == 'D' or s[i+1] == 'M') {
                            res += -100;
                        }
                        else {
                            res += 100;
                        }
                    }
                    break;
                case 'D':
                    res += 500;
                    break;
                case 'M':
                    res += 1000;
                    break;
            }
        }
        return res;
    }
};