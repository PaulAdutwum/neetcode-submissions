# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Input: 
        Given a list node to of integers stored in reverse 
        order 

        Goal is return the the sum of digits where each node will 
        only contain a single digit

        The goal is the retun the sum of two numbers in the list

        Example'
         321 = 1 -> 2 -> 3
         684 = 4 -> 8 -> 6
        ans:   5 -> 0 -> 0 - 1  

        """
        dummy = ListNode()
        current = dummy
        carry = 0 

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry

            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next 

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None


        return dummy.next  


    

        






        