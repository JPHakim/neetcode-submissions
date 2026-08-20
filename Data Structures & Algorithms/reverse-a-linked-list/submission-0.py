# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stk = []
        reverse = ListNode()
        curr = head
        while curr:
            stk.append(curr.val)
            curr = curr.next
        tail = reverse
        while stk:
            tail.next = ListNode(stk.pop())
            tail = tail.next
        return reverse.next
            
        