# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#O(n),O(1)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        second = head
        dummy = ListNode()
        dummy.next = head
        first = dummy
        count = 0
        while count<n and second:
            second = second.next
            count+=1
        while second:
            second= second.next
            first = first.next    
        if first.next:
            first.next = first.next.next
           
        # length = 0
        # curr = head
        # while curr:
        #     length += 1
        #     curr = curr.next
        # length -= n
        # temp = head
        # while length>1:
        #     temp = temp.next
        #     length -=1
        # if temp.next:
        #     temp.next = temp.next.next

        return dummy.next        

        
