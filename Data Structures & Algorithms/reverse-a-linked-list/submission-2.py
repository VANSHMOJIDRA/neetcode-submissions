# Definition for singly-linked list.
# class listnode:
#    def listnode(self,val = 0,next=None):
#       self.val = val
#        self.next = next

class Solution:
    def reverseList(self,head:Optional[Listnode])-> Optional[listnode]:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev