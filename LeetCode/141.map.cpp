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

        std::map<ListNode*, bool> visited;
        while(head){
            visited[head] = true;
            if (visited[head->next]){
                return true;
            }
            head = head->next;
        }
        return false;
    }
};
