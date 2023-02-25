class Solution {
    public String getHint(String secret, String guess) {
        int bulls = 0, cows = 0, n = secret.length();
        int[] used = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
        for(int i = 0; i < n; ++i) {
            if(secret.charAt(i) == guess.charAt(i))
                ++bulls;
            else
                used[secret.charAt(i)-'0'] += 1;
        }
        for(int i = 0; i < n; ++i) {
            if(secret.charAt(i) != guess.charAt(i) && used[guess.charAt(i)-'0'] > 0) {
                ++cows;
                --used[guess.charAt(i)-'0'];
            }
        }
        return bulls + "A" + cows + "B";
    }
}