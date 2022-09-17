#include <limits.h>

int dig(char c) {
    switch(c) {
        case '0':
            return 0;
        case '1':
            return 1;
        case '2':
            return 2;
        case '3':
            return 3;
        case '4':
            return 4;
        case '5':
            return 5;
        case '6':
            return 6;
        case '7':
            return 7;
        case '8':
            return 8;
        case '9':
            return 9;
        case '-':
            return -1;
        case '+':
            return -1;
        case ' ':
            return -4;
        default:
            return -2;
    }
}

int myAtoi(char * s) {
    long int i = 0, c = 1, n = 0;
    bool b = false;
    while(s[i] != '\0') {
        switch(dig(s[i])) {
            case -2:
                if(b) {
                    return c * n;
                }
                else {
                    return 0;
                }
                i++;
                break;
            case -4:
                if(b) {
                    return c * n;
                }
                i++;
                break;
            case -1:
                if(b) {
                    return c*n;
                }
                b = true;
                if(dig(s[i + 1]) >= 0) {
                    if(s[i] == '-'){
                        c = -1;
                    }
                }
                i++;
                break;
            default:
                b = true;
                n = n * 10 + dig(s[i]);
                i++;
                if(n*c > INT_MAX) {
                    return INT_MAX;
                }
                if(n*c < INT_MIN) {
                    return INT_MIN;
                }
                break;
        }
    }
    return c * n;
}