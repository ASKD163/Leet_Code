class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return
        self.invertTree(root.left)                  #反转左子树
        self.invertTree(root.right)                 #反转右子树
        root.left,root.right = root.right,root.left
        return root
