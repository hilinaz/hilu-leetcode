class MyLinkedList:

    def __init__(self):
        self.head=None
        

    def get(self, index: int) -> int:
        curr = self.head
        count =0
        while curr:
            if count!=index:
                curr=curr.next
                count+=1
            else:
                return curr.val
        return -1

        

    def addAtHead(self, val: int) -> None:
        Node = ListNode(val)
        Node.next=self.head
        self.head=Node

        

    def addAtTail(self, val: int) -> None:
        dummy=ListNode()
        dummy.next=self.head
        Node = ListNode(val)
        curr = dummy
        while curr and curr.next:
            curr=curr.next
        curr.next=Node
        self.head= dummy.next
        
        

    def addAtIndex(self, index: int, val: int) -> None:

        count =0 
        curr =self.head
        Node =ListNode(val)
        if index==0:
            self.addAtHead(val)
            return
        
        while curr:
            if count==index-1:
                Node.next=curr.next
                curr.next=Node
                return self.head
            curr=curr.next
            count+=1
        

    def deleteAtIndex(self, index: int) -> None:
        dummy=ListNode()
        dummy.next=self.head
        curr =dummy
        count =0
        while curr and curr.next:
            if count==index:
                curr.next=curr.next.next
                break
            count+=1
            curr=curr.next
        self.head=dummy.next
             


        
        

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)