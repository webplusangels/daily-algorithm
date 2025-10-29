# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        odd_list = ListNode(val=head.val, next=None)
        new_head = ListNode(val=0, next=odd_list)
        head = head.next

        # even_list = ListNode(val=head.val, next=None)
        even_list = ListNode(val=0)
        even_head = even_list
        # even_head = ListNode(val=0, next=even_list)
        # head = head.next

        i = 1
        while head != None:
            new_node = ListNode(val=head.val)

            if i % 2:
                even_list.next = new_node
                even_list = even_list.next
            else:
                odd_list.next = new_node
                odd_list = odd_list.next
                
            i += 1
            head = head.next
        
        # odd_list.next가 가리키는 노드는 even_head의 next         
        odd_list.next = even_head.next        

        return new_head.next