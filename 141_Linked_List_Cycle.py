class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head:ListNode) -> bool:
        seen = set()
        i = 0
        while head:
            if head in seen:
                return i
            i += 1
            seen.add(head)
            head = head.next
