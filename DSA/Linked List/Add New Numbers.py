# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        carry = 0
        temp = dummy
        while l1 and l2:
            ans = l1.val+l2.val+carry
            if ans>9:
                carry = 1
                ans %=10
            else:
                carry=0    
            temp.next = ListNode(ans,None)
            l1,l2,temp = l1.next,l2.next,temp.next
        while l1:
            ans = l1.val+carry
            if ans>9:
                carry = 1
                ans %=10
            else:
                carry=0    
            temp.next = ListNode(ans,None)
            l1,temp = l1.next,temp.next
        while l2:
            ans = l2.val+carry
            if ans>9:
                carry = 1
                ans %=10
            else:
                carry=0    
            temp.next = ListNode(ans,None)
            l2,temp=l2.next,temp.next
        if carry==1:
            temp.next=ListNode(carry,None)
        return dummy.next         



#Good Code:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        carry = 0
        temp = dummy
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            ans = v1+v2+carry
            carry = ans//10
            ans %=10    
            temp.next = ListNode(ans,None)
            temp = temp.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next         




        

        
