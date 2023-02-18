/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if(head == nullptr)
            return nullptr;
        
        Node *res, *res_head, *og_head = head;
        res = new Node(0);
        res_head = res;
        
        vector<Node *> rands, addr, new_addr;
        while(head) {
            res->next = new Node(head->val);
            res = res->next;
            
            if(head->random)
                rands.push_back(head->random);
            else
                rands.push_back(nullptr);
            addr.push_back(head);
            new_addr.push_back(res);
            
            head = head->next;
        }
        res_head = res_head->next;
        res = res_head;
        head = og_head;
        
        for(int i = 0; i < rands.size(); ++i) {
            int randindex = find(addr.begin(), addr.end(), rands[i]) - addr.begin();
            if(randindex != rands.size()) {
                res->random = new_addr[randindex];
            }
            res = res->next;
        }
        
        return res_head;
    }
};