# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s=set()
        a=headA
        b=headB
        while a:
            s.add(a)
            a=a.next
        while b:
            if b in s:
                return b
            s.add(b)
            b=b.next
        