class Solution {
public:
    int minCost(vector<int>& startPos, vector<int>& homePos, vector<int>& rowCosts, vector<int>& colCosts) {
        int res = 0;
        if(homePos[0] < startPos[0]) {
            res = accumulate(rowCosts.begin() + homePos[0], rowCosts.begin() + startPos[0], 0);
        }
        else {
            res = accumulate(rowCosts.begin() + startPos[0] + 1, rowCosts.begin() + homePos[0] + 1, 0);
        }
        if(homePos[1] < startPos[1]) {
            res += accumulate(colCosts.begin() + homePos[1], colCosts.begin() + startPos[1], 0);
        }
        else {
            res += accumulate(colCosts.begin() + startPos[1] + 1, colCosts.begin() + homePos[1] + 1, 0);
        }
        return res;
    }
};