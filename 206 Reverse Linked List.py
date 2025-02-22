'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.aux(head, None)

    def aux(self, head, previous):
        if head is None:
            return previous  

        reversed_list = self.aux(head.next, head)

        head.next = previous

        return reversed_list
