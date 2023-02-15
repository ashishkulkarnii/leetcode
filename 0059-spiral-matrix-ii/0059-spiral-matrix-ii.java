class Solution {
    public int[][] generateMatrix(int n) {
        int[][] arr = new int[n][n];
        int x = 0, y = 0;
        char direction = 'e';
        for(int i = 1; i <= n * n; ++i) {
            arr[y][x] = i;
            switch(direction) {
                case 'e':
                    if(x + 1 != n && arr[y][x+1] == 0) {
                        ++x;
                    } else {
                        ++y;
                        direction = 's';
                    }
                    break;
                case 's':
                    if(y + 1 != n && arr[y+1][x] == 0) {
                        ++y;
                    } else {
                        --x;
                        direction = 'w';
                    }
                    break;
                case 'w':
                    if(x - 1 >= 0 && arr[y][x-1] == 0) {
                        --x;
                    } else {
                        --y;
                        direction = 'n';
                    }
                    break;
                case 'n':
                    if(y - 1 >= 0 && arr[y-1][x] == 0) {
                        --y;
                    } else {
                        ++x;
                        direction = 'e';
                    }
                    break;
            }
        }
        return arr;
    }
}