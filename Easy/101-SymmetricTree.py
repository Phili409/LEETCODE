# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def helper(tree1: TreeNode, tree2: TreeNode):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
        return False
    
    if tree1.left == tree2.right and tree2
    
class Solution:
    def isSymmetric(self, root:TreeNode) -> bool:
        if root.left is None and root.right is None:
            return True
        if root.left is None or root.right is None:
            return False
        
        if root.left.val == root.right.val:
            return self.isSymmetric(root.left) and self.isSymmetric(root.right)
        return False