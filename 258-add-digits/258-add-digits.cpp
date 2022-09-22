class Solution {
public:
    int addDigits(int num) {
        if(num < 10) {
            return num;
        }
        else {
            int temp = 0;
            while(num > 0) {
                temp += num % 10;
                num = num / 10;
            }
            return addDigits(temp);
        }
    }
};