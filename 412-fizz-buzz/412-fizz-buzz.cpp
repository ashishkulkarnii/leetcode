class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> res;
        for(int i = 1; i <= n; i++) {
            if(not(i % 3 or i % 5)) {
                res.push_back("FizzBuzz");
            }
            else if(not(i % 3)) {
                res.push_back("Fizz");
            }
            else if(not(i % 5)) {
                res.push_back("Buzz");
            }
            else {
                res.push_back(to_string(i));
            }
        }
        return res;
    }
};