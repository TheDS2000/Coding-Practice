# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#O(k*n),O(1)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeList(l1:Optional[ListNode],l2:Optional[ListNode]):
            dummy = ListNode(0)
            tail = dummy
            while l1 and l2:
                if l1.val<l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            if l1:
                tail.next=l1
            if l2:
                tail.next=l2

            return dummy.next
        ans = None
        for i in range(len(lists)):
            ans = mergeList(ans,lists[i])   
        return ans             

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#O(n* logk), O(1)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeList(l1:Optional[ListNode],l2:Optional[ListNode]):
            dummy = ListNode(0)
            tail = dummy
            while l1 and l2:
                if l1.val<l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            if l1:
                tail.next=l1
            if l2:
                tail.next=l2

            return dummy.next
        ans = None
        for i in range(len(lists)):
            ans = mergeList(ans,lists[i])   
        return ans             

        
        
