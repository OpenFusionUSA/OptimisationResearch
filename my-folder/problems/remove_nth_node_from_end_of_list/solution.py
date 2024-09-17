# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        hair=head
        tor=head
        for _ in range(n):
            hair=hair.next
        if not hair:
            return head.next
        while hair.next:
            tor=tor.next
            hair=hair.next
        tor.next=tor.next.next
        return head