from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        node, preNode = head, None
        leftNode, rightNode = None, None
        index = 1

        while node != None:
            if (index == left):
                ## store left-1, left
                leftNode = (preNode, node)

            if (index == right):
                ## store right-1, right
                rightNode = (preNode, node)

            preNode = node
            node = node.next
            index += 1

        print('left', leftNode)
        print('right', rightNode)

        ## chain right side
        temp = leftNode[1].next
        leftNode[1].next = rightNode[1].next
        rightNode[1].next = temp

        ## chain left side
        rightNode[0].next = leftNode[1]
        if (leftNode[0] != None):
            leftNode[0].next = rightNode[1]

        print(head)
        return head

if __name__ == "__main__":
    head, left, right = [1,2,3,4,5], 2, 4
    # head, left, right = [5], 1, 1
    print(Solution().reverseBetween(input, left, right))

