# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#O(n)
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if k==0:
            return head    
        leng = 1
        temp = head
        while temp.next:
            temp = temp.next
            leng+=1
        k = k%leng
        temp.next = head
        end = leng-k
        while end>0:
            temp = temp.next
            end -=1
        head=temp.next
        temp.next = None

        return head        
                


        
