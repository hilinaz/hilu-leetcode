# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        if not head:
            return []
        if not head.next:
            return [0]
        curr= head
        nums=[]
        while curr:
            nums.append(curr.val)
            curr=curr.next
        stack =[]
        ans =[0]*len(nums)
        for i,val in enumerate(nums):
            while stack and val>nums[stack[-1]]:
                index=stack.pop()
                ans[index]=val
            stack.append(i)
            
        return ans


        

            


      

        