Link : 206. Reverse Linked List https://leetcode.com/problems/reverse-linked-list/description/
Iterative solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# TC:O(n), SC: O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head
        curr = head
        prev = None
        while curr !=None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev    

Recursive Solution
#TC:O(n), SC:O(n)
        
