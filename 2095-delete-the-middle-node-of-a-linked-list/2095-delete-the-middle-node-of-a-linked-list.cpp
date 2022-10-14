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
    ListNode* deleteMiddle(ListNode* head) {
        ListNode* temp = head;
        int len = 0;
        while(temp != NULL) {
            ++len;
            temp = temp->next;
        }
        if(len == 0 or len == 1) {
            return NULL;
        }
        if(len == 2) {
            head->next = NULL;
            return head;
        }
        temp = head;
        for(int _ = 0; _ < (int) len / 2; ++_) {
            temp = temp->next;
        }
        if(temp->next != NULL) {
            temp->val = temp->next->val;
            temp->next = temp->next->next;
        }
        return head;
    }
};