class SubrectangleQueries {
    int[][] r;

    public SubrectangleQueries(int[][] rectangle) {
        r = rectangle;
    }
    
    public void updateSubrectangle(int row1, int col1, int row2, int col2, int newValue) {
        for(int x = col1; x <= col2; ++x) {
            for(int y = row1; y <= row2; ++y) {
                r[y][x] = newValue;
            }
        }
    }
    
    public int getValue(int row, int col) {
        return r[row][col];
    }
}

/**
 * Your SubrectangleQueries object will be instantiated and called as such:
 * SubrectangleQueries obj = new SubrectangleQueries(rectangle);
 * obj.updateSubrectangle(row1,col1,row2,col2,newValue);
 * int param_2 = obj.getValue(row,col);
 */