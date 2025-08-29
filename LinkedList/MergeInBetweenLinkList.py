# You are given two linked lists: list1 and list2 of sizes n and m respectively.
#
# Remove list1's nodes from the ath node to the bth node, and put list2 in their place.
from LinkedList.ListNode import ListNode

class MergeInBetweenLinkList:
    def mergeInBetweenLinkList(self,list1: ListNode,a:int,b:int,list2: ListNode):
        curr = list1
        i = 0

        while i < a-1:
            curr = curr.next

        head = curr

        while i <= b:
            curr = curr.next
            i = i +1

        head.next = list2

        while list2.next:
            list2 = list2.next

        list2.next = curr

        return list1


