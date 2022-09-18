class Solution {
public:
    int maxDistToClosest(vector<int>& seats) {
        for(int i = 0; i < seats.size(); i++){
            cout<<seats[i]<<' ';
        }
        cout<<endl;
        
        vector<int> left = seats;
        int d = seats.size();
        for(int i = 0; i < seats.size(); i++){
            if(seats[i] == 1){
                left[i] = 0;
                d = 1;
            }
            else if(seats[i] == 0){
                if(d != seats.size()){
                    left[i] = d++;
                }
            }
        }
        
        for(int i = 0; i < seats.size(); i++){
            cout<<left[i]<<' ';
        }
        cout<<endl;
        
        d = seats.size();
        vector<int> right = seats;
        for(int i = seats.size() - 1; i > -1; i--){
            if(seats[i] == 1){
                right[i] = 0;
                d = 1;
            }
            else if(seats[i] == 0){
                if(d != seats.size()){
                    right[i] = d++;
                }
            }
        }
        
        for(int i = 0; i < seats.size(); i++){
            cout<<right[i]<<' ';
        }
        
        int res = 1, temp;
        for(int i = 0; i < seats.size(); i++){
            if(right[i] == 0){
                temp = left[i];
            }
            else if(left[i] == 0){
                temp = right[i];
            }
            else{
                temp = left[i] > right[i] ? right[i] : left[i];
            }
            res = temp > res ? temp : res;
        }
        
        return res;
    }
};