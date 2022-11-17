class Solution {
public:
    bool compare(int a, int b) {
        return a < b;
    }
    int computeArea(int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2, int by2) {
        int a = (ax2 - ax1) * (ay2 - ay1), b = (bx2 - bx1) * (by2 - by1), ox = 0, oy = 0;
        if(bx1 < ax1) {
            if(bx2 > ax1 and bx2 < ax2) {
                ox = bx2 - ax1;
            }
            else if(bx2 >= ax2) {
                ox = ax2 - ax1;
            }
        }
        else if(bx1 >= ax1 and bx1 < ax2) {
            if(bx2 <= ax2) {
                ox = bx2 - bx1;
            }
            else {
                ox = ax2 - bx1;
            }
        }
        if(by1 < ay1) {
            if(by2 > ay1 and by2 < ay2) {
                oy = by2 - ay1;
            }
            else if(by2 >= ay2) {
                oy = ay2 - ay1;
            }
        }
        else if(by1 >= ay1 and by1 < ay2) {
            if(by2 <= ay2) {
                oy = by2 - by1;
            }
            else {
                oy = ay2 - by1;
            }
        }
        return a + b - ox * oy;
    }
};