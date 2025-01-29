class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head:ListNode) -> ListNode:
        length = 0
        m = head
        point = head
        while point:
            length += 1
            if length % 2 == 0:
                m = m.next
            point = point.next
        return m

def printLL(ll: ListNode) -> None:
    while ll:
         print(ll.val)
         ll = ll.next
     

printLL(middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))

