class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        val = head
        
        while val and val.next:
            if val.val == val.next.val:
                val.next = val.next.next
            else:
                val = val.next
        
        return head