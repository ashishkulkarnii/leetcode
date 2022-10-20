class Solution {
public:
    int countPrimes(int n) {
        if(n == 0 or n == 1) {
            return 0;
        }
        bool prime[n];
        for(auto &e: prime) {
            e = true;
        }
        for(int i = 2; i < n; i++) {
            if(prime[i] == true) {
                for(int j = 2 * i; j < n; j += i) {
                    prime[j] = false;
                }
            }
        }
        return count(prime + 2, prime + n, true);
    }
};