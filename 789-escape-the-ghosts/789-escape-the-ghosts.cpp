class Solution {
public:
    bool escapeGhosts(vector<vector<int>>& ghosts, vector<int>& target) {
        int cg = abs(target[0] - ghosts[0][0]) + abs(target[1] - ghosts[0][1]);
        for(auto c: ghosts) {
            cg = min(cg, abs(target[0] - c[0]) + abs(target[1] - c[1]));
        }
        return cg > abs(target[0]) + abs(target[1]);
    }
};