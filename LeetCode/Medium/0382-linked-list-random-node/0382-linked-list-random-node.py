import random

items = [1, 2, 3, 4, 5]
result = random.choice(items)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.lst = []
        while head:
            self.lst.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return random.choice(self.lst)


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()