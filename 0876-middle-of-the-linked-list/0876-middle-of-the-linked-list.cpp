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
    ListNode* middleNode(ListNode* head) {
        if(head->next == NULL)
            return head;
        ListNode *middle = head, *last = head;
        while(last->next != NULL and last->next->next != NULL) {
            last = last->next->next;
            middle = middle->next;
        }
        if(last->next == NULL)
            return middle;
        else
            return middle->next;
    }
};