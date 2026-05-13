# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        count = 0
        curr = head 
        
        while curr:
            count += 1
            curr = curr.next 


        rem_node = count - n
        prev = dummy
        for _ in range(rem_node):
            prev = prev.next 

        prev.next = prev.next.next 

        return dummy.next 

          
        