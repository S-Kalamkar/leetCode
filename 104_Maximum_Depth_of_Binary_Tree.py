class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: TreeNode) -> int:
        def recur(branch):
            if branch:
                return 1 + max(recur(branch.left), recur(branch.right))
            else:
                return 0
        return recur(root)

tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(maxDepth(tree))