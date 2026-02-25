# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = None
        ptr = None
        pq = []
        for i, listHead in enumerate(lists):
            if listHead is None:
                continue
            heapq.heappush(pq, (listHead.val, i))

        while pq:
            val, i = heapq.heappop(pq)
            if head is None:
                head = lists[i]
                ptr = head
            else:
                ptr.next = lists[i]
                ptr = ptr.next

            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(pq, (lists[i].val, i))

        return head
        
