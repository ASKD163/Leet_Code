#递归
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def DFS(root):
            if not root:
                return
            DFS(root.left)
            DFS(root.right)
            res.append(root.val)
        res = []
        DFS(root)
        return res
        
        
#迭代
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        que = [root]
        while que:
            tmp = que.pop()
            res.append(tmp.val)

            if tmp.left:
                que.append(tmp.left)
            if tmp.right:
                que.append(tmp.right)

        res.reverse()
        return res
