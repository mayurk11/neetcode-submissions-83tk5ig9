# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        temp = head
         
        while temp is not None:
            length +=1
            temp = temp.next

        if length == n:
            new_head = head.next
            return new_head

            
        position_to_stop = length - n - 1
        count = 0
        temp = head

        while count < position_to_stop:
            temp = temp.next
            count +=1
        temp.next = temp.next.next
        return head

