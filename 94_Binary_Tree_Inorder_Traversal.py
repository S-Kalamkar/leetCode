class treeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    read = []
    def recur(curr, read):
        if not curr:
            return
        recur(curr.left, read)
        read.append(curr.val)
        recur(curr.right, read)
        
    recur(root, read)
    return read

root = treeNode(1, treeNode(2, treeNode(4), treeNode(5, treeNode(6), treeNode(7))), treeNode(3, None, treeNode(8, treeNode(9))))
print(inorderTraversal(root))