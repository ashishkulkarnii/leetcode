class Solution {
public:
    int ans=0,empty=1;
    
    void solve(int i,int j,vector<vector<int>>& grid,int ct)
    {
        if(i<0|| j<0 ||j>=grid[0].size()||i>=grid.size()|| grid[i][j]==-1)
        return;
        if(grid[i][j]==2)
        {
            if(ct==empty)
            ans++;
            return;
        }
      grid[i][j]=-1;
      solve(i,j+1,grid,ct+1);
      solve(i,j-1,grid,ct+1);
      solve(i+1,j,grid,ct+1);
      solve(i-1,j,grid,ct+1);
      grid[i][j]=0;
    }
    
    int uniquePathsIII(vector<vector<int>>& grid) 
    {
        int start_x=0,start_y=0,n=grid[0].size(),m=grid.size();
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(grid[i][j]==1)
                {
                    start_x=i,start_y=j;
                }
                else
                if(grid[i][j]==0)
                empty++;
            }
        }
        solve(start_x,start_y,grid,0);
        return ans;
    }
};
