#遍历二叉数
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#DFS
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def DFS(root,tmp):
            if root:
                tmp += str(root.val)
                if not root.left and not root.right:
                    res.append(tmp)
                    return
                else:
                    DFS(root.left, tmp + '->')
                    DFS(root.right, tmp + '->')
        

        res = []
        DFS(root,'')
        return res
