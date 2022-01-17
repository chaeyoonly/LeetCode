# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# One Pointer
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr, length = head, 0
        while ptr:
            ptr, length = ptr.next, length + 1
        if length == n : return head.next
        ptr = head
        for i in range(1, length - n):
            ptr = ptr.next
        ptr.next = ptr.next.next
        return head

      
# Discuss
# Two Pointers
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        for i in range(n):
            fast = fast.next
        if not fast: return head.next
        while fast.next:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head
