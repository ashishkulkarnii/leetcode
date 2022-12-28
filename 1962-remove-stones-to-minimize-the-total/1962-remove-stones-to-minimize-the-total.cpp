class Solution {
public:
    int minStoneSum(vector<int>& piles, int k) {
        priority_queue<int> pq;
        for(auto s: piles) {
            pq.push(s);
        }
        int temp;
        for(int i = 0; i < k; ++i) {
            temp = pq.top();
            pq.pop();
            pq.push(temp - temp/2);
        }
        temp = 0;
        while(not pq.empty()) {
            temp += pq.top();
            pq.pop();
        }
        return temp;
    }
};