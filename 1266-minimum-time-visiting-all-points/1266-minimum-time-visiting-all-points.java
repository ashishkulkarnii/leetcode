class Solution {
    public int minTimeToVisitAllPoints(int[][] points) {
        int xi = points[0][0], yi = points[0][1], x, y, res = 0, dx, dy, temp;
        for(int i = 0; i < points.length; ++i) {
            x = points[i][0]; y = points[i][1];
            dx = Math.abs(x - xi); dy = Math.abs(y - yi);
            temp = Math.max(dx, dy);
            res += temp;
            dx -= temp; dy -= temp;
            if(dx > 0) {
                res += dx;
            }
            if(dy > 0) {
                res += dy;
            }
            xi = x; yi = y;
        }
        return res;
    }
}
