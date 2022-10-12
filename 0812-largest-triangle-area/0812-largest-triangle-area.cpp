class Solution {
public:
    double area(vector<int> p1, vector<int> p2, vector<int> p3) {
        double a = sqrt(pow((p1[0] - p2[0]), 2) + pow((p1[1] - p2[1]), 2));
        double b = sqrt(pow((p2[0] - p3[0]), 2) + pow((p2[1] - p3[1]), 2));
        double c = sqrt(pow((p3[0] - p1[0]), 2) + pow((p3[1] - p1[1]), 2));
        double s = (a + b + c) / 2;
        double area = sqrt(s * (s - a) * (s - b) * (s - c));
        return area;
    }
    double largestTriangleArea(vector<vector<int>>& points) {
        double res = area(points[0], points[1], points[2]);
        for(int i = 0; i < points.size() - 2; ++i) {
            for(int j = 0; j < points.size() - 1; ++j) {
                for(int k = 0; k < points.size(); ++k) {
                    res = max(res, area(points[i], points[j], points[k]));
                }
            }
        }
        return res;
    }
};