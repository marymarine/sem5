"""Task 5: Dijkstra's algorithm"""
INF = 1000000

class Graph:
    """Describes undirected connected weighted graph"""
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

    def dijkstra(self, nodeStart, nodeEnd):
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

        #print the shortest walk
        curr_v = nodeEnd
        walk = []
        while curr_v != nodeStart:
            walk.append(curr_v)
            curr_v = prev[curr_v]
        walk.append(curr_v)
        print(*reversed(walk))
        print("distance = ", dist[nodeEnd])

g = Graph([[0, 3, 5], [1, 3, 11], [2, 3, 56], [4, 3, 77],[5, 4, 89]])
print("Type start and end vertices:")
v_start = int(input())
v_end = int(input())
g.dijkstra(v_start, v_end)
