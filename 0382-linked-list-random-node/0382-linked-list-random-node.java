/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
import java.lang.Math;

class Solution {
    ListNode head;
    int len = 0;
    
    public Solution(ListNode head1) {
        head = head1;
        len = getLength(head);
    }
    
    public int getRandom() {
        ListNode node = head;
        int x = (int) Math.floor((double) len * Math.random());
        for(int i = 0; i < x; ++i)
            node = node.next;
        return node.val;
    }
    
    private int getLength(ListNode head) {
        int res = 0;
        while(head != null) {
            head = head.next;
            ++res;
        }
        return res;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */