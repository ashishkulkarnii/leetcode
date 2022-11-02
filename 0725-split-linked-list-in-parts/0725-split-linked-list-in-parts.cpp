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
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        vector<ListNode*> result;
        ListNode* temp = head;
        int len = 0, lengths[k];
        while(temp != NULL) {
            temp = temp->next;
            ++len;
        }
        temp = head;
        int rem = len % k;
        for(int i = 0; i < k; ++i) {
            lengths[i] = len / k;
            if(rem > 0) {
                ++lengths[i];
                --rem;
            }
        }
        result.push_back(head);
        for(int i = 1; i < k; ++i) {
            if(lengths[i] == 0) {
                result.push_back(NULL);
                continue;
            }
            cout<<head->val;
            for(int j = 0; j < lengths[i-1]-1; ++j) {
                temp = temp->next;
            }
            head = temp->next;
            temp->next = NULL;
            temp = head;
            result.push_back(head);
        }
        return result;
    }
};