class Solution {
    public int minPathSum(int[][] grid) {
        int[] dfs = grid[0];
        for(int col = 1; col < grid[0].length; ++col) {
            dfs[col] += dfs[col-1];
        }
        for(int row = 1; row < grid.length; ++row) {
            dfs[0] += grid[row][0];
            for(int col = 1; col < grid[0].length; ++col) {
                dfs[col] = grid[row][col] + Math.min(dfs[col], dfs[col-1]);
            }
        }
        return dfs[dfs.length-1];
    }
}