class Solution {
public:
    int finalBallPos(vector<vector<int>>& grid, int col) {
        int curr_col = col, curr_row = 0;
        while(curr_row < grid.size()) {
            switch(grid[curr_row][curr_col]) {
                case 1:
                    if(curr_col + 1 < grid[0].size()) {
                        if(grid[curr_row][curr_col+1] == 1) {
                            ++curr_col;
                            ++curr_row;
                        }
                        else {
                            return -1;
                        }
                    }
                    else {
                        return -1;
                    }
                    break;
                case -1:
                    if(curr_col - 1 >= 0) {
                        if(grid[curr_row][curr_col-1] == -1) {
                            --curr_col;
                            ++curr_row;
                        }
                        else {
                            return -1;
                        }
                    }
                    else {
                        return -1;
                    }
                    break;
            }
        }
        return curr_col;
    }
    vector<int> findBall(vector<vector<int>>& grid) {
        vector<int> result;
        for(int i = 0; i < grid[0].size(); ++i) {
            result.push_back(finalBallPos(grid, i));
        }
        return result;
    }
};