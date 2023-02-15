class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> list = new ArrayList<Integer>();
        int x = 0, y = 0, n = matrix.length, m = matrix[0].length;
        char direction = 'e';
        for(int i = 1; i <= n * m; ++i) {
            list.add(matrix[y][x]);
            matrix[y][x] = 1000;
            switch(direction) {
                case 'e':
                    if(x + 1 != m && matrix[y][x+1] != 1000) {
                        ++x;
                    } else {
                        ++y;
                        direction = 's';
                    }
                    break;
                case 's':
                    if(y + 1 != n && matrix[y+1][x] != 1000) {
                        ++y;
                    } else {
                        --x;
                        direction = 'w';
                    }
                    break;
                case 'w':
                    if(x - 1 >= 0 && matrix[y][x-1] != 1000) {
                        --x;
                    } else {
                        --y;
                        direction = 'n';
                    }
                    break;
                case 'n':
                    if(y - 1 >= 0 && matrix[y-1][x] != 1000) {
                        --y;
                    } else {
                        ++x;
                        direction = 'e';
                    }
                    break;
            }
        }
        return list;
    }
}