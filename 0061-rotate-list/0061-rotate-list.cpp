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
    ListNode* rotateRight(ListNode* head, int k) {
        if(k == 0) {
            return head;
        }
        ListNode* temp = head, *ihead = head;
        int len = 0;
        while(temp != NULL) {
            temp = temp->next;
            ++len;
        }
        if(len == 0 or len == 1) {
            return ihead;
        }
        k = k % len;
        if(k == 0) {
            return ihead;
        }
        temp = head;
        for(int i = 0; i < len - k; ++i) {
            temp = temp->next;
        }
        ListNode* first = temp;
        while(temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = ihead;
        for(int i = 0; i < len - k; ++i) {
            temp = temp->next;
        }
        temp->next = NULL;
        return first;
    }
};