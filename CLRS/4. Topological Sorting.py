__author__ = 'Mj'
import copy

def topo(graph, source, L):
    visited.append(source)
    if source not in graph:
        return None
    for node in graph[source]:
        if node in visited:
            print("Cycle present between", source, "&", node)
            return None
        if node not in visited:
            topo(graph, node, L)
    L.append(source)

Graph = {}
visited = []
visit = []
L = []
numEdges = int(input().strip())
for i in range(numEdges):
    n1, n2 = list(map(int, input().strip().split()))
    Graph.setdefault(n1, []).append(n2)
so = int(input("Enter source: "))
topo(Graph, so, L)
visited.reverse()
visit = copy.deepcopy(visited)
print(visit)
visited[:] = []
print(visit)
for n in Graph:
    if n not in visit:
        topo(Graph, n, L)
        visited.reverse()
        for node in visited:
            if node not in visit:
                visit.append(node)
print(L)
visit.reverse()
print(visit)