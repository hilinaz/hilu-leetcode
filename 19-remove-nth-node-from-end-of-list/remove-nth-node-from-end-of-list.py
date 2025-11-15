# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy= ListNode()
        dummy.next=head
        head=dummy
        aheadpt =head
        while n>0:
            aheadpt=aheadpt.next
            n-=1
        behindpt=head
        while aheadpt and aheadpt.next:
            aheadpt=aheadpt.next
            behindpt= behindpt.next
        behindpt.next=behindpt.next.next
        return dummy.next
    