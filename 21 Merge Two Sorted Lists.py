'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 == None and list2 != None:
            result_list = list2

        elif list1 != None and list2 == None:
            result_list = list1

        elif list1 == None and list2 == None:
            return None
        
        else:
            if list1.val < list2.val:
                result_list = list1
                self.aux(list1.next, list2, result_list)
            else:
                result_list = list2
                self.aux(list1, list2.next, result_list)
        
        return result_list
        
        

    def aux(self, list1, list2, result_list):
        if list1 is None and list2 is not None:
            result_list.next = list2

        elif list1 is not None and list2 is None:
            result_list.next = list1

        elif list1 is None and list2 is None:
            pass

        else:
            if list1.val < list2.val:
                result_list.next = list1
                self.aux(list1.next, list2, result_list.next)

            else:
                result_list.next = list2
                self.aux(list1, list2.next, result_list.next)

        return result_list
