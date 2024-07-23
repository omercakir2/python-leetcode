#In this code , my purpose is to merge 2 linked integer list which are ordered by decreasing order
#Also to learn how to manage linked lists.



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Firstly , it's needed to be checked if there is 2 linked list //
        if not list1:
            return list2 
        if not list2:
            return list1
        
        # If there's , we need to find out the which one will be the first node // 

        if list1.val < list2.val:
            first_node = list1
            list1 = list1.next
        else :
            first_node = list2
            list2 = list2.next
        current = first_node

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1=list1.next
            else:
                current.next = list2
                list2=list2.next
            current = current.next
        if list1:
            current.next = list1
        else:
             current.next = list2
        return first_node
        
        
        

        