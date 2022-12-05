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
    int pairSum(ListNode* head) {
        vector<int> list;
        while(head != NULL) {
            list.push_back(head->val);
            head = head->next;
        }
        int n = list.size(), mts = -1;
        for(int i = 0; i <= (n/2) - 1; ++i) {
            mts = max(mts, list[i] + list[n-1-i]);
        }
        return mts;
    }
};