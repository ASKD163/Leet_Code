class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        que = [root]

        while(que):
            size = len(que)
            tmp = que + [None]
            for i in range(size):
                tmp[i].next = tmp[i+1]
            for J in range(size):
                Node = que.pop(0)
                if Node.left: 
                    que.append(Node.left)
                if Node.right:
                    que.append(Node.right)
        return root
