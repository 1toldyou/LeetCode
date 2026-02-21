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
        Node* newHead = nullptr;
        map<Node*, Node*> nodes;

        Node* curr = head;
        Node* prev = nullptr;

        while(curr){
            nodes[curr] = new Node(curr->val);

            if (!newHead){
                newHead = nodes[curr];
            }

            if (prev){
                prev->next = nodes[curr];
            }
            prev = nodes[curr];
            curr = curr->next;
        }

        curr = head;
        while(curr){
            nodes[curr]->random = nodes[curr->random];
            curr = curr->next;
        }

        return newHead;
    }
};
