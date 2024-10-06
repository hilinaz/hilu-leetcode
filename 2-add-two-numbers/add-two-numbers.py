class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1,l2):
        result_head = ListNode(0)
        current_node = result_head
        carry = 0

        while l1 is not None or l2 is not None or carry > 0:
            value1 = l1.val if l1 is not None else 0
            value2 = l2.val if l2 is not None else 0
            total = value1 + value2 + carry
            
            carry = total // 10
            current_node.next = ListNode(total % 10)
            current_node = current_node.next
            
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return result_head.next