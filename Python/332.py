#安排行程
#欧拉图

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res = []
        Map = collections.defaultdict(list)
        for f,t in tickets:# 构建邻接表
            Map[f] += [t] 
        for f in Map:
            Map[f].sort()#排序
        
        def dfs(node):
            while Map[node]:
                dfs(Map[node].pop(0))
            res.insert(0,node)

          

        dfs('JFK') 
        return res
