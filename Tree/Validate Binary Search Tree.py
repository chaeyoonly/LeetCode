# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorderTree(root: Optional[TreeNode], l: List[int]):
            if not root:
                return
            inorderTree(root.left, l)
            l.append(root.val)
            inorderTree(root.right, l)
        l = list()
        inorderTree(root, l)
        
        if l == sorted(l) == sorted(set(l)):
            return True
        else:
            return False
        
