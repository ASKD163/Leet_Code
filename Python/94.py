#递归
#先访问左子树
#根节点
#右子树
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def Midorder(root):
            if root != None:
                Midorder(root.left)
                res.append(root.val)
                Midorder(root.right)
            
        res = []
        Midorder(root)
        return res
        
#迭代效率大于递归
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res
