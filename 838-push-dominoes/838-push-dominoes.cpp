class Solution {
public:
    string pushDominoes(string dominoes) {
        string prev;
        do {
            prev = dominoes;
            for(int i = 0; i < dominoes.length(); i++) {
                if(i != 0) {
                    if(dominoes[i] == 'L') {
                        if(dominoes[i-1] == '.') {
                            dominoes[i-1] = 'l';
                        }
                        else if(dominoes[i-1] == 'r') {
                            dominoes[i-1] = '.';
                        }
                    }
                }
                if(i != dominoes.length() - 1) {
                    if(dominoes[i] == 'R') {
                        if(dominoes[i+1] == '.') {
                            dominoes[i+1] = 'r';
                        }
                    }
                }
            }
            for(int i = 0; i < dominoes.length(); i++) {
                if(dominoes[i] == 'l') 
                    dominoes[i] = 'L';
                if(dominoes[i] == 'r')
                    dominoes[i] = 'R';
            }
        } while(prev != dominoes);
        return dominoes;
    }
};