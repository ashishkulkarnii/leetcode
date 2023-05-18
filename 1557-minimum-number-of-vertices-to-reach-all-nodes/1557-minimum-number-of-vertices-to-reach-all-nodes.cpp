class Solution {
public:
    vector<int> findSmallestSetOfVertices(int n, vector<vector<int>>& edges) {
        set<int> res;
        for(int i = 0; i < n; ++i) {
            res.insert(i);
        }
        for(auto edge: edges) {
            res.erase(edge[1]);
        }
        vector<int> ans(res.begin(), res.end());
        return ans;
    }
};