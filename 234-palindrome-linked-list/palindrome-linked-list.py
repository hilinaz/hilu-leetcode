# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev = None 
        left = head 

        fast = head 
        while fast and fast.next:
            fast = fast.next.next
            temp = left.next
            left.next=prev
            prev=left
            left= temp
        if fast:
            left = left.next
         
        
        right = left
        left = prev
      
        

        while left and right:
            if left.val!=right.val:
                return False
            left = left.next
            right = right.next
           
        return True

        









                                                              

                                                                                      

         




 




  


  





          
    

         
     
       


        
        