# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
       
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while prev.next:
            current = prev.next
            # Check if current node is a start of duplicates
            while current.next and current.val == current.next.val:
                current = current.next
            if prev.next != current:
                # Skip all duplicates
                prev.next = current.next
            else:
                prev = prev.next

        return dummy.next
