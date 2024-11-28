# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy_node = ListNode()
        head = dummy_node
        while list1 and list2:
            if list1.val < list2.val:
                dummy_node.next = list1
                list1 = list1.next

            else:
                dummy_node.next = list2
                list2 = list2.next

            dummy_node = dummy_node.next

        if list1:
            dummy_node.next = list1

        if list2:
            dummy_node.next = list2

        return head.next
    

if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    s = Solution()
    result = s.mergeTwoLists(l1, l2)
    while result:
        print(result.val, end=' ')
        result = result.next
    print()

                