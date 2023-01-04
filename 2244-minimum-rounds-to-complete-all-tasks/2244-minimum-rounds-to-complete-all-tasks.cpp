class Solution {
public:
    int minimumRounds(vector<int>& tasks) {
        unordered_map<int, int> t;
        int res = 0;
        for(auto x: tasks) {
            if(t.find(x) == t.end())
                t[x] = 1;
            else
                t[x] += 1;
        }
        for(auto x: t) {
            if(x.second == 1)
                return -1;
            else
                res += x.second / 3 + (x.second - 3 * floor(x.second / 3) == 1 || x.second - 3 * floor(x.second / 3) == 2);
        }
        return res;
    }
};