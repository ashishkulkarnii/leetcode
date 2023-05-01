class Solution {
public:
    double average(vector<int>& salary) {
        double sum = 0;
        int min_sal = salary[0], max_sal = salary[0];
        for(auto sal: salary) {
            min_sal = sal < min_sal ? sal : min_sal;
            max_sal = sal > max_sal ? sal : max_sal;
            sum += sal;
        }
        double tmp = sum - min_sal - max_sal;
        return tmp > 0 ? tmp / (salary.size() - 2) : 0;
    }
};