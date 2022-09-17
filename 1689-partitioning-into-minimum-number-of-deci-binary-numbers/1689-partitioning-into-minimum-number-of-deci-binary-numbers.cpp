class Solution {
public:
    int atoi(char c) {
        return (int) c - 48;
    }
    int minPartitions(string n) {
        int res = 0;
        for(int i = 0; i < n.length(); i++){
            if(res == 9){
                return 9;
            }
            if(atoi(n[i]) > res){
                res = atoi(n[i]);
            }
        }
        return res;
    }
};