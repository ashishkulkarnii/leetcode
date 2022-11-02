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
    ListNode* oddEvenList(ListNode* head) {
        if(head == NULL) {
            return head;
        }
        else if(head->next == NULL) {
            return head;
        }
        ListNode* odd_first = head;
        ListNode* even_first = head->next;
        ListNode* curr = odd_first;
        ListNode* curr2 = even_first;
        while(curr->next != NULL) {
            cout<<curr->val<<' ';
            if(curr->next->next != NULL) {
                curr->next = curr->next->next;
                curr = curr->next;
                if(curr2->next->next != NULL) {
                    curr2->next = curr2->next->next;
                    curr2 = curr2->next;
                }
            }
            else {
                break;
            }
        }
        curr2->next = NULL;
        curr->next = even_first;
        return odd_first;
    }
};