import java.util.regex.Matcher;
import java.util.regex.Pattern;

class Solution {
    public boolean checkString(String s) {
        return Pattern.compile("a*b*", Pattern.CASE_INSENSITIVE).matcher(s).matches();
    }
}