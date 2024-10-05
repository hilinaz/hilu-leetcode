class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def add(self, value, lists):
        listnew = ListNode(value)
        if lists is None:
            return listnew
        else:
            current = lists
            while current:
                if current.next is None:
                    current.next = listnew
                    break
                current = current.next
        return lists

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        newlist = None

        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    newlist = ListNode(list1.val) if newlist is None else newlist.add(list1.val, newlist)
                    list1 = list1.next
                else:
                    newlist = ListNode(list2.val) if newlist is None else newlist.add(list2.val, newlist)
                    list2 = list2.next
            elif list1:
                newlist = ListNode(list1.val) if newlist is None else newlist.add(list1.val, newlist)
                list1 = list1.next
            elif list2:
                newlist = ListNode(list2.val) if newlist is None else newlist.add(list2.val, newlist)
                list2 = list2.next

        return newlist