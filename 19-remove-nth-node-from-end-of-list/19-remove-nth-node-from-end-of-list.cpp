/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* last = head;
        ListNode* first = head;
        ListNode* pf; // node before one to be deleted
                
        for(int i = 0; i < n; i++) {
            last = last->next;
        }
        
        while(last != NULL) {
            last = last->next;
            pf = first;
            first = first->next;
        }
        
        if(first == head) { // if first node is to be deleted
            head = head->next;
        }
        else {
            pf->next = first->next;
        }
        
        return head;
    }
};