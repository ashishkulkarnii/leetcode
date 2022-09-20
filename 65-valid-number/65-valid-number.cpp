class Solution {
public:
    bool isNumber(string s) {
        bool dot = false, num = false, br = true, e = false;
        int i = 0;
        while(i < s.length() and br) {
            switch(s[i]) {
                case 'e':
                case 'E':
                    e = true;
                    if(not num) {
                        return false;
                    }
                    br = false;
                    break;
                case '+':
                case '-':
                    if(i != 0) {
                        return false;
                    }
                    break;
                case '.':
                    if(dot) {
                        return false;
                    }
                    dot = true;
                    break;
                case '0':
                case '1':
                case '2':
                case '3':
                case '4':
                case '5':
                case '6':
                case '7':
                case '8':
                case '9':
                    num = true;
                    break;
                default:
                    return false;
            }
            i++;
        }
        int temp = i;
        if(not num) {
            return false;
        }
        if(not br and num) {
            int j = 0;
            bool op = false;
            num = false;
            while(i < s.length()){
                switch(s[i]) {
                    case '+':
                    case '-':
                        if(j != 0 ) {//or op) {
                            return false;
                        }
                        op = true;
                        break;
                    case '0':
                    case '1':
                    case '2':
                    case '3':
                    case '4':
                    case '5':
                    case '6':
                    case '7':
                    case '8':
                    case '9':
                        num = true;
                        break;
                    default:
                        return false;
                }
                j++;
                i++;
            }
            if(op and not num) {
                return false;
            }
        }
        if(e and temp == i) {
            return false;
        }
        else {
            return true;
        }
        
    }
};
