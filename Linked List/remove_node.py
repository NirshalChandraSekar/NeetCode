# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        length = 1
        second = head.next
        while second:
            second = second.next
            length += 1

        node = length - n 
        
        if node == 0:
            return head.next
        
        current = head
        for i in range(node-1):
            current = current.next

        current.next = current.next.next

        return head
    
if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)

    s = Solution()
    result = s.removeNthFromEnd(l1, 2)
    while result:
        print(result.val, end=' ')
        result = result.next
    print()
    