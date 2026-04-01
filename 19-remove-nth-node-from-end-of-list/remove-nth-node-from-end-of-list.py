# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy= ListNode(0)
        dummy.next= head
        head = dummy

        ahead = head
        while n>0:
            ahead=ahead.next
            n-=1
        behind= head 
        while ahead and ahead.next:
            behind= behind.next
            ahead = ahead.next
        behind.next = behind.next.next
        return dummy.next
        

  
  
       
 
 



       
      



 



 
        


       







  
        