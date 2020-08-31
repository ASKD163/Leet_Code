#dfs 
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        N = len(rooms)
        memo = set([0])

        def dfs(keys):
            for i in keys:
                if i in memo or i == None:
                    continue
                else:
                    memo.add(i)
                    dfs(rooms[i])

        dfs(rooms[0])
        return N == len(memo)
        
#bfs
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        N = len(rooms)
        memo,tmp = {0}, [0]

        while tmp:
            visted = tmp.pop()
            for i in rooms[visted]:
                if i not in memo:
                    tmp.insert(0,i)
                    memo.add(i)

        return N == len(memo)
