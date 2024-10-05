# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        linked=head
        pre=None
        while linked:
            nextnode=linked.next
            linked.next=pre
            pre=linked
            linked=nextnode
        return pre
            
        