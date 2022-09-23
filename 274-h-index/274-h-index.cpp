class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = citations.size();
        sort(citations.begin(), citations.end());
        int h = 0;
        for(int i = 0; i < n; i++) {
            if(citations[i] >= n - i) {
                h = (n - i > h) ? n - i : h;
            }
        }
        return h;
    }
};