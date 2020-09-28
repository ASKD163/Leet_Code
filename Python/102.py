class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        que = [root]
        res = []
        while que:
            size = len(que)
            tmp = []
            for i in range(size):
                node = que.pop(0)
                tmp.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(tmp)
        return res
