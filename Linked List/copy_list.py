"""
# Definition for a Node."""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        
        old2new = {}
        copy_head = Node(head.val)
        iter_ = head.next
        copy_iter = copy_head
        old2new[head] = copy_head
        
        while iter_:
            value = iter_.val
            copy_iter.next = Node(value)
            copy_iter = copy_iter.next
            old2new[iter_] = copy_iter
            iter_ = iter_.next

        for key, value in old2new.items():
            value.random = old2new[key.random] if key.random else None




if __name__ == "__main__":
    l1 = Node(7)
    l1.next = Node(13)
    l1.next.next = Node(11)
    l1.next.next.next = Node(10)
    l1.next.next.next.next = Node(1)

    l1.next.random = l1
    l1.next.next.random = l1.next.next.next.next
    l1.next.next.next.random = l1.next.next 
    l1.next.next.next.next.random = l1
    l1.random = None

    s = Solution()
    s.copyRandomList(l1)
