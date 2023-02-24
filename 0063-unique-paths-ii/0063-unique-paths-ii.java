class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int[] dp = new int[obstacleGrid[0].length];
        for(int i = 0; i < dp.length; ++i) {
            if(obstacleGrid[0][i] == 1)
                dp[i] = 0;
            else {
                if(i == 0)
                    dp[i] = 1;
                else
                    dp[i] = dp[i-1];
            }
        }
        for(int y = 1; y < obstacleGrid.length; ++y) {
            if(obstacleGrid[y][0] == 1)
                dp[0] = 0;
            for(int x = 1; x < obstacleGrid[0].length; ++x) {
                if(obstacleGrid[y][x] == 1)
                    dp[x] = 0;
                else
                    dp[x] += dp[x-1];
            }
        }
        return dp[dp.length - 1];
    }
}