'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        wallhack = [n]
        head = self.aux(head, wallhack)
        if head is None:
            return None
        elif wallhack[0] > 0:
            return head.next
        return head
        

    def aux(self, head, wallhack):
        if head.next is None:
            return None

        self.aux(head.next, wallhack)
        wallhack[0] -= 1
        if wallhack[0] == 0:
            head.next = head.next.next
        
        return head
