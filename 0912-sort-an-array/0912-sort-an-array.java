import java.util.HashMap;
import java.lang.Math;

class Solution {
    public int[] sortArray(int[] nums) {
        HashMap<Integer, Integer> counter = new HashMap<>();
        int min_val = nums[0], max_val = nums[0], index = 0;
        for(int n: nums) {
            if(counter.containsKey(n))
                counter.put(n, counter.get(n) + 1);
            else
                counter.put(n, 1);
            min_val = Math.min(min_val, n);
            max_val = Math.max(max_val, n);
        }
        for(int i = min_val; i <= max_val; ++i) {
            while(counter.containsKey(i) && counter.get(i) > 0) {
                nums[index++] = i;
                counter.put(i, counter.get(i) - 1);
            }
        }
        return nums;
    }
}