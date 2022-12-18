class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temps) {
        int n = temps.size();
        stack<int> st;
        vector<int> answer(n, 0);
        for(int i = n - 1; i >= 0; --i) {
            while(not(st.empty() or temps[st.top()] > temps[i]))
                st.pop();
            if(not st.empty())
                answer[i] = st.top() - i;
            st.push(i);
        }
        return answer;
    }
};