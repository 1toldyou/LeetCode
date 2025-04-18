/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (!head){
            return false;
        }

        if (!head->next){
            return false;
        }

        std::vector<ListNode*> visited;
        while(head){
            visited.push_back(head);
            for (auto existing : visited){
                if (existing == head->next){
                    return true;
                }
            }
            head = head->next;
        }
        return false;
    }
};
