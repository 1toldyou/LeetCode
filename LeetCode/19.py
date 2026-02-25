# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        if length - n == 0:
            return head.next

        node = head
        i = 0
        while i < length - n - 1:
            i += 1
            node = node.next

        if node.next:
            print("removing", node.next.val)
            node.next = node.next.next

        return head
        
        
