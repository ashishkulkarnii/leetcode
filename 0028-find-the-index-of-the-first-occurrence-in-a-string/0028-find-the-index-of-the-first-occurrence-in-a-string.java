class Solution {
    public int strStr(String haystack, String needle) {
        boolean found;
        for(int i = 0; i < haystack.length() - needle.length() + 1; ++i) {
            found = true;
            for(int j = 0; j < needle.length(); ++j) {
                if(haystack.charAt(i + j) != needle.charAt(j)) {
                    found = false;
                    break;
                }
            }
            if(found) {
                return i;
            }
        }
        return -1;
    }
}