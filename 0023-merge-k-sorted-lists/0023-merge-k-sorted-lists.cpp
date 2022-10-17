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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if(lists.size() == 0) {
            return NULL;
        }
        int min_index = -1;
        for(int i = 0; i < lists.size(); ++i) {
            if(lists[i] != NULL) {
                min_index = i;
                break;
            }
        }
        if(min_index == -1) {
            return NULL;
        }
        ListNode *result, *head;
        for(int i = min_index; i < lists.size(); i++) {
            if(lists[i] != NULL) {
                if(lists[min_index]->val > lists[i]->val) {
                    min_index = i;
                }
            }
        }
        result = lists[min_index];
        head = result;
        lists[min_index] = lists[min_index]->next;
        while(true) {
            min_index = -1;
            for(int i = 0; i < lists.size(); ++i) {
                if(lists[i] != NULL) {
                    min_index = i;
                    break;
                }
            }
            if(min_index == -1) {
                break;
            }
            for(int i = min_index; i < lists.size(); i++) {
                if(lists[i] != NULL) {
                    if(lists[min_index]->val > lists[i]->val) {
                        min_index = i;
                    }
                }
            }
            result->next = lists[min_index];
            result = result->next;
            lists[min_index] = lists[min_index]->next;
        }
        return head;
    }
};