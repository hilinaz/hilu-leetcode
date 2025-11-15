# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count =0
        curr = head
        while curr:
            count+=1
            curr=curr.next
        index= count-n
        pt =0
        dummy=ListNode()
        dummy.next=head
        head=dummy
        curr= dummy
        while curr and curr.next:
            if pt==index:
                curr.next=curr.next.next
                break
            pt+=1
            curr=curr.next
        return dummy.next

        
        