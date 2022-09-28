class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        int res = 0;
        for(int j = 0; j < jewels.length(); j++) {
            for(int s = 0; s < stones.length(); s++) {
                res += jewels[j] == stones[s] ? 1 : 0;
            }
        }
        return res;
    }
};