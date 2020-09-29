class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return
        que = [root]
        res = []
        while que:
            size = len(que)
            tmp = que
            Sum = 0
            for i in range(size):
                tmp = que.pop(0)
                Sum += tmp.val
                
                if tmp.left:
                    que.append(tmp.left)
                if tmp.right:
                    que.append(tmp.right)
            res.append(Sum/size)

        return res
