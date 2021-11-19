class Solution:
    def reverseList(self, head):
        prev = None
        current = head
        while head:
            current = head
            head = head.next
            current.next = prev
            prev = current
        return prev
      
      
# # 디버깅
#     while head: # 1,2,3,4,5
#         curr = head # 1->2->3->4->5
#         head = head.next # 2->3->4->5
#         curr.next = prev # curr 1->None
#         prev = curr # prev 1->None
#     while head: # 2,3,4,5
#         curr = head # 2->3->4->5
#         head = head.next # 3->4->5
#         curr.next = prev # curr 2->prev(1->None)
#         prev = curr # prev 2->1->None
#     while head: # 3,4,5
#         curr = head # 3->4->5
#         head = head.next # 4->5
#         curr.next = prev # curr 3->prev(2->1->None)
#         prev = curr # prev 3->2->1->None
