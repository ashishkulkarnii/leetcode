/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* last = head;
        ListNode* first = head;
        ListNode* pf;
                
        for(int i = 0; i < n; i++) {
            last = last->next;
        }
        
        while(last != NULL) {
            last = last->next;
            pf = first;
            first = first->next;
        }
        
        if(first == head) {
            head = head->next;
        }
        else {
            pf->next = first->next;
        }
        
        return head;
    }
};