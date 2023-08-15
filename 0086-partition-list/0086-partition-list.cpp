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
    ListNode* partition(ListNode* head, int x) {
        ListNode* curr = head;
        ListNode* prev;
        if(!head) return head;
        if(head->val >= x) {
            prev = curr;
            curr = curr->next;
            while(curr) {
                if(curr->val < x) {
                    prev->next = curr->next;
                    curr->next = head;
                    head = curr;
                    break;
                }
                else {
                    prev = curr;
                    curr = curr->next;
                }
            }
        }
        curr = head->next; prev = head;
        ListNode* last_small = head;
        while(curr) {
            if(curr->val < x) {
                if(last_small->next == curr) {
                    last_small = curr;
                }
                else {
                    prev->next = curr->next;
                    curr->next = last_small->next;
                    last_small->next = curr;
                    last_small = curr;
                    curr = prev;
                }
            }
            cout<<curr->val;
            prev = curr;
            curr = curr->next;
        }
        return head;
    }
};