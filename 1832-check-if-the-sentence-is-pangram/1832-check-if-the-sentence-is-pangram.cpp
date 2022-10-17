class Solution {
public:
    bool checkIfPangram(string sentence) {
        bool a[26] = {false};
        for(auto c: sentence) {
            a[(int) c - 97] = true;
        }
        return find(a, a + 26, 0) == a + 26;
    }
};