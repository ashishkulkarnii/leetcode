class Solution {
public:
    int minTimeToVisitAllPoints(vector<vector<int>>& points) {
        int x, y, xi = points[0][0], yi = points[0][1], dx, dy, temp, res = 0;
        for(int i = 1; i < points.size(); ++i) {
            x = points[i][0]; y = points[i][1];
            dx = abs(x - xi); dy = abs(y - yi);
            temp = max(dx, dy);
            dx -= temp; dy -= temp;
            res += temp + (dx > 0 ? dx : 0) + (dy > 0 ? dy : 0);
            xi = x; yi = y;
        } 
        return res;
    }
};