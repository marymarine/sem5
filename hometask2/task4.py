"""Task 4: Graph"""
class Graph:
    """Describes undirected connected graph"""
    def __init__(self, list_of_edges):
        """Create an adjacency list of graph"""
        self.adj_vertices = []
        i = 0
        while i < len(list_of_edges):
            while len(self.adj_vertices) <= list_of_edges[i][0] or len(self.adj_vertices) <= list_of_edges[i][1]:
                self.adj_vertices.append([])
            self.adj_vertices[list_of_edges[i][0]].append(list_of_edges[i][1])
            self.adj_vertices[list_of_edges[i][1]].append(list_of_edges[i][0])
            i += 1
        self.length = len(self.adj_vertices)
        self.is_visited = [False]*self.length

    def clean(self):
        """Make all vertices as not visited"""
        self.is_visited = [False] * self.length

    def dfs(self, vertex):
        """Deapth-first search"""
        self.is_visited[vertex] = True
        print(vertex)
        for v in self.adj_vertices[vertex]:
            if not self.is_visited[v]:
                self.dfs(v)

    def bfs(self, vertex):
        """Breadth-first search"""
        self.is_visited[vertex] = True
        queue = [vertex]
        while queue:
            current_vertex = queue.pop(0)
            print(current_vertex)
            for v in self.adj_vertices[current_vertex]:
                if not self.is_visited[v]:
                    queue.append(v)
                    self.is_visited[v] = True

g = Graph([[0, 3], [1, 3], [2, 3], [4, 3], [5, 0]])
print("DFS algorithm:")
g.dfs(0)
g.clean()
print("BFS algorithm:")
g.bfs(0)
