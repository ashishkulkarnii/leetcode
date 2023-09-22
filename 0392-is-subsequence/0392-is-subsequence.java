class Solution {
    public boolean isSubsequence(String s, String t) {
        int len = s.length();
        if(len == 0)
            return true;
        int i = 0;
        for(char c: t.toCharArray()) {
            if(s.charAt(i) == c)
                ++i;
            if(i == len)
                break;
        }
        return i == len;
    }
}