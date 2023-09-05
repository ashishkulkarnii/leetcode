/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    private int getNodePos(Node head, Node target) {
        int pos = 0;
        while(head != null) {
            if(head == target)
                return pos;
            else {
                ++pos;
                head = head.next;
            }
        }
        return pos;
    }

    private Node getNodeAtPos(Node head, int pos) {
        while(pos > 0) {
            head = head.next;
            --pos;
        }
        return head;
    }

    public Node copyRandomList(Node head) {
        if(head == null)
            return null;

        Node original_head = head, new_head = new Node(head.val);
        Node curr = new_head;
        
        head = head.next;
        while(head != null) {
            curr.next = new Node(head.val);
            curr = curr.next;
            head = head.next;
        }
        curr = new_head;
        head = original_head;

        while(head != null) {
            if(head.random == null)
                curr.random = null;
            else
                curr.random = getNodeAtPos(new_head, getNodePos(original_head, head.random));
            head = head.next;
            curr = curr.next;
        }

        return new_head;
    }
}