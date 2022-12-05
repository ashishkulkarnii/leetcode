class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
        sort(skill.begin(), skill.end());
        int n = skill.size();
        long long res = 0, team_skill = -1;
        for(int i = 0; i < n/2; ++i) {
            if(team_skill == -1)
                team_skill = skill[i] + skill[n-i-1];
            else
                if(team_skill != skill[i] + skill[n-i-1])
                    return -1;
            res += skill[i] * skill[n-i-1];
        }
        return res;
    }
};