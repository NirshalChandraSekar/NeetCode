# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        head_1 = l1
        head_2 = l2
        carry = 0
        new_head = None
        iter_node = None
        while head_1 or head_2:
            first = head_1.val if head_1 else 0
            second = head_2.val if head_2 else 0
            sum = first + second + carry
            value_to_insert = sum % 10

            if new_head is None:
                new_head = ListNode(value_to_insert)
                iter_node = new_head

            else:
                iter_node.next = ListNode(value_to_insert)
                iter_node = iter_node.next

            carry = int(sum / 10)

            head_1 = head_1.next if head_1 else None
            head_2 = head_2.next if head_2 else None

        if carry > 0:
            iter_node.next = ListNode(carry)

        return new_head
    
if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    s = Solution()
    result = s.addTwoNumbers(l1, l2)
    print("Result:")
    while result:
        print(result.val)
        result = result.next
        