# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ptr = head
        tail = None
        n = 0
        while ptr:
            n += 1
            tail = ptr
            ptr = ptr.next
        if n <= 1:
            return head

        k %= n
        if k == 0:
            return head

        # nth node from the end
        ptr = head
        i = 0
        while i < n-k-1: 
            ptr = ptr.next
            i += 1
        target = ptr.next
        ptr.next = None
        tail.next = head

        return target
