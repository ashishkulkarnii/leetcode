class Solution {
public:
    string addBinary(string a, string b) {
        int i = a.length() - 1, j = b.length() - 1;
        bool carry = 0;
        string res = "";
        while(i >= 0 and j >= 0) {
            if(a[i] == '1' and b[j] == '0' or a[i] == '0' and b[j] == '1') {
                if(carry == 0) {
                    res = "1" + res;
                }
                else {
                    res = "0" + res;
                }
            }
            else if(a[i] == '0' and b[j] == '0') {
                if(carry == 0) {
                    res = "0" + res;
                }
                else {
                    res = "1" + res;
                    carry = 0;
                }
            }
            else {
                if(carry == 0) {
                    carry = 1;
                    res = "0" + res;
                }
                else {
                    res = "1" + res;
                }
            }
            --i, --j;
        }
        if(j == -1) {
            b = a;
            j = i;
        }
        while(j >= 0) {
            if(b[j] == '0') {
                if(carry == 0) {
                    res = "0" + res;
                }
                else {
                    res = "1" + res;
                    carry = 0;
                }
            }
            if(b[j] == '1') {
                if(carry == 0) {
                    res = "1" + res;
                }
                else {
                    res = "0" + res;
                }
            }
            --j;
        }
        if(carry == 1) {
            res = "1" + res;
        }
        return res;
    }
};