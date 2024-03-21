# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        slow,fast = dummy,dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            return slow.next
        return slow    



#Optimised Good code
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        return slow    

        
