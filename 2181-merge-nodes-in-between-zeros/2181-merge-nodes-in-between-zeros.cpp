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
    ListNode* mergeNodes(ListNode* head) {
        ListNode* result = new ListNode();
        ListNode* res = result;
        int temp = 0;
        while(head != NULL) {
            if(head->val == 0) {
                if(temp != 0) {
                    res->next = new ListNode();
                    res = res->next;
                    res->val = temp;
                    temp = 0;
                }
                head = head->next;
            }
            else {
                temp += head->val;
                head = head->next;
            }
        }
        return result->next;
    }
};