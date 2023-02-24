class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int[] dp = new int[obstacleGrid[0].length];
        dp[0] = 1;
        for(int y = 0; y < obstacleGrid.length; ++y) {
            if(obstacleGrid[y][0] == 1)
                dp[0] = 0;
            for(int x = 1; x < obstacleGrid[0].length; ++x)
                dp[x] = (dp[x-1] + dp[x]) * (1 - obstacleGrid[y][x]);
        }
        return dp[dp.length-1];
    }
}