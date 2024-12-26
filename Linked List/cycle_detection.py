# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False
    
if __name__ == "__main__":
    l1 = ListNode(3)
    l1.next = ListNode(2)
    l1.next.next = ListNode(0)
    l1.next.next.next = ListNode(-4)
    l1.next.next.next.next = l1.next

    s = Solution()
    result = s.hasCycle(l1)
    print("Result:", result)