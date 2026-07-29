# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = []
        current = head
        while current:
            nodes.append(current)
            if current.next in nodes:
                return True 
            current = current.next
        return False 
        