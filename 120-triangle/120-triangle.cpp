class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int min;
        for(int i = 1; i < triangle.size();i++){
            for(int j = 0;j<triangle[i].size();j++){
                if(j==0){
                    triangle[i][j] += triangle[i-1][j];
                }
                else if(j==triangle[i].size()-1){
                    triangle[i][j] += triangle[i-1][j-1];
                }
                else{
                    int t1 = triangle[i-1][j-1];
                    int t2 = triangle[i-1][j];
                    triangle[i][j] += (t1>t2)?t2:t1;
                }
            }
        }
        min = triangle[triangle.size()-1][0];
        for(int i = 0; i < triangle[triangle.size()-1].size();i++){
            if(min > triangle[triangle.size()-1][i]){
                min = triangle[triangle.size()-1][i];
            }
        }
        return min;
    }
};

// def minimumTotal(self, triangle: List[List[int]]) -> int:
//         for i in range(1, len(triangle)):
//             for j in range(len(triangle[i])):
//                 if j == 0:
//                     triangle[i][j] += triangle[i-1][0]
//                 elif j == len(triangle[i]) - 1:
//                     triangle[i][j] += triangle[i-1][len(triangle[i-1]) - 1]
//                 else:
//                     t1 = triangle[i-1][j-1]
//                     t2 = triangle[i-1][j]
//                     triangle[i][j] += min([t1,t2])
//         return(min(triangle[-1]))
