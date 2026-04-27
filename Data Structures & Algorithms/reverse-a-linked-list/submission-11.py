# class node:
# def __init__(self,val,next):
# self.val = val
# self.next = next

class Solution:
    def reverseList(self,head:Optional(ListNode))-> Optional(ListNode):
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev