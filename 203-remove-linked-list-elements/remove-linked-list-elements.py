# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        # the value could be at any point including the head
        dummy = ListNode()
        dummy.next=head
        head = dummy 
        prev =dummy
        curr = dummy.next
        while curr:
            if curr.val==val:
                prev.next=curr.next

            else:
                prev=prev.next
            curr=curr.next
        return dummy.next
            
            

        



        
        