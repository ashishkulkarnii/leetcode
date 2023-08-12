class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        vector<int> dp = obstacleGrid[0];
        dp[0] = 1;
        for(int y = 0; y < obstacleGrid.size(); ++y) {
            if(obstacleGrid[y][0] == 1)
                dp[0] = 0;
            for(int x = 1; x < obstacleGrid[0].size(); ++x)
                dp[x] = (dp[x-1] + dp[x]) * (1 - obstacleGrid[y][x]);
        }
        return dp[dp.size()-1];
    }
};