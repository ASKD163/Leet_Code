#递归
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def DFS(root):
            if not root:
                return
            res.append(root.val)
            DFS(root.left)
            DFS(root.right)
        
        res = []
        DFS(root)
        return res

#迭代
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        que = [root]
        res = []
        while que:
            tmp = que.pop()
            res.append(tmp.val)
            if tmp.right:
                que.append(tmp.right)
            if tmp.left:
                que.append(tmp.left)
            
        return res
