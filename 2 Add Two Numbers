'''
    You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.find_number(l1)
        l2 = self.find_number(l2)
        result = int(l1) + int(l2)
        result = str(result)
        print(result)

        return self.create_linked_list(result)

    def find_number(self, listNode):
        if not isinstance(listNode.next, ListNode):
            return str(listNode.val)

        else:
            return self.find_number(listNode.next) + str(listNode.val)

    def create_linked_list(self, result):
        if len(result) == 1:
            return ListNode(int(result), None)
        
        else:
            return ListNode(int(result[-1]), self.create_linked_list(result[:-1]))
