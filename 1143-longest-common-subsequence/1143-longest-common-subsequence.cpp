class Solution {
public:
    int longestCommonSubsequence(string t1, string t2) {
        short dp[1000][1000];
        for(short i = 0; i < t1.length(); ++i)
            for(short j = 0; j < t2.length(); ++j)
                dp[i+1][j+1] = (t1[i] == t2[j]) ? (dp[i][j] + 1) : (max(dp[i][j+1], dp[i+1][j]));
        return dp[t1.length()][t2.length()];
    }
};