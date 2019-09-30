"""Task 6: Delay time"""
INF = 1000000

class Graph:
    """Describes directed connected weighted graph"""
    def __init__(self, edges):
        """Create graph"""
        self.adj = []
        i = 0
        while i < len(edges):
            while len(self.adj) <= edges[i][0] or len(self.adj) <= edges[i][1]:
                self.adj.append([])
            i += 1
        self.is_visited = [False]*len(self.adj)

        i = 0
        while i < len(self.adj):
            j = 0
            while j < len(self.adj):
                self.adj[i].append([j, INF])
                j += 1
            i += 1

        i = 0
        while i < len(edges):
            self.adj[edges[i][0]][edges[i][1]][1] = edges[i][2]
            self.adj[edges[i][1]][edges[i][0]][1] = edges[i][2]
            i += 1

    def dijkstra(self, nodeStart):
        """Executes Dijksta's algotithm"""
        prev = []
        dist = []
        #set dist to zero for initial node and to infinity for all other nodes
        for i in range(len(self.adj)):
            prev.append(-1)
            dist.append(INF)
        dist[nodeStart] = 0

        for i in range(len(self.adj)):
            #seach not visited node with min dist
            v = -1
            for j in range(len(self.adj)):
                if not self.is_visited[j] and ( v == -1 or dist[j] < dist[v]):
                    v = j
            #mark current node visited
            self.is_visited[v] = True
            #change dist
            for j in range(len(self.adj[v])):
                u = self.adj[v][j][0]
                weight = self.adj[v][j][1]
                if dist[v] + weight < dist[u]:
                    dist[u] = dist[v] + weight
                    prev[u] = v

        #print time
        for i in range(len(self.adj)):
            if prev[i] == -1 and i != 0 and i != nodeStart:
                print("-1")
                return
        max = 0
        for j in range(1, len(self.adj)):
            if dist[j] > max:
                max = dist[j]
        print(max)

times = Graph([[2,1,1],[2,3,1],[3,4,1]])
X = 2
times.dijkstra(X)