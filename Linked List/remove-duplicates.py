# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = value = head
        if not head: return head
        while head.next:
            value = head.next
            if head.val == value.val:
                head.next = value.next
            else:
                head = head.next
        return dummy
