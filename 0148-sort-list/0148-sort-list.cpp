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
    ListNode* sortList(ListNode* head) {
        list<int> arr;
        ListNode* temp = head;
        while(temp != NULL) {
            arr.push_back(temp->val);
            temp = temp->next;
        }
        arr.sort();
        temp = head;
        while(temp != NULL) {
            temp->val = arr.front();
            arr.pop_front();
            temp = temp->next;
        }
        return head;
    }
};