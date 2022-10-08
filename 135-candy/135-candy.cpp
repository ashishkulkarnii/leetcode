class Solution {
public:
    int candy(vector<int>& ratings) {
        int n = ratings.size();
        if(n == 1) {
            return 1;
        }
        vector<int> candies(n, 0);
        for(int i = 0; i < n; ++i) {
            if(i == 0) {
                candies[i] += 0;
            }
            else {
                if(ratings[i-1] < ratings[i]) {
                    candies[i] += candies[i-1] + 1;
                }
                else {
                    candies[i] += 0;
                }
            }
        }
        for(auto c: candies) {
            cout<<c<<' ';
        }
        cout<<endl;
        for(int i = n - 1; i >= 0; --i) {
            if(i == n - 1) {
                candies[i] += 0;
            }
            else {
                if(ratings[i+1] < ratings[i]) {
                    if(candies[i] <= candies[i+1]) {
                        candies[i] = candies[i+1] + 1;
                    }
                }
                else {
                    candies[i] += 0;
                }
            }
        }
        for(auto c: candies) {
            cout<<c<<' ';
        }
        cout<<endl;
        int offset = 1 - *min_element(candies.begin(), candies.end());
        return accumulate(candies.begin(), candies.end(), offset * n);
    }
};