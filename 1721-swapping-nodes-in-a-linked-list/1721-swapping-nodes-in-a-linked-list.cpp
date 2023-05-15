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
    ListNode* swapNodes(ListNode* head, int k) {
        --k;
        ListNode *kth, *curr = head;
        int len = -1;
        while(curr) {
            curr = curr->next;
            ++len;
        }
        if(k > len / 2)
            k = len - k;
        curr = head;
        for(int i = 0; i < k; ++i) {
            curr = curr->next;
        }
        kth = curr;
        curr = kth;
        for(int i = 0; i < len - 2 * k; ++i) {
            curr = curr->next;
        }
        swap(curr->val, kth->val);
        return head;
    }
};