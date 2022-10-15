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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *head;
        head = new ListNode((l1->val + l2->val) % 10);
        int carry = (l1->val + l2->val - (l1->val + l2->val) % 10) / 10;
        l1 = l1->next; l2 = l2->next;
        ListNode *temp = head;
        while(l1 != NULL and l2 != NULL) {
            temp->next = new ListNode((l1->val + l2->val + carry) % 10);
            carry = (l1->val + l2->val + carry - (l1->val + l2->val + carry) % 10) / 10;
            temp = temp->next;
            l1 = l1->next; l2 = l2->next;
        }
        if(l1 == NULL) {
            swap(l1, l2);
        }
        while(l1 != NULL) {
            temp->next = new ListNode((l1->val + carry) % 10);
            carry = (l1->val + carry - (l1->val + carry) % 10) / 10;
            temp = temp->next;
            l1 = l1->next;
        }
        if(carry == 1) {
            temp->next = new ListNode(1);
        }
        return head;
    }
};