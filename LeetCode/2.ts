/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    if (!l1 || !l2){
        return null;
    }

    let carryOver = 0;
    let head;
    let curr;
    while(l1 || l2){
        let v1 = 0;
        let v2 = 0;
        if (l1){
            v1 = l1.val;
            l1 = l1.next;
        }
        if (l2){
            v2 = l2.val;
            l2 = l2.next;
        }
        let currSum = carryOver + v1 + v2;
        if (currSum >= 10){
            carryOver = 1;
            currSum = currSum - 10;
        }
        else {
            carryOver = 0;
        }

        let newNode = new ListNode(currSum);
        if (curr){
            curr.next = newNode;
            curr = newNode;
        }
        else {
            head = newNode;
            curr = newNode;
        }
    }

    if (carryOver > 0){
        curr.next = new ListNode(1);
    }

    if (head){
        return head;
    }
    else {
        return new ListNode(0);
    }
};
