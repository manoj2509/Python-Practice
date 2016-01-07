__author__ = 'Mj'
import copy
# Global Counter.
count = 0

# General DFS function.
def DFS(graph, source):
    global count
    count += 1
    visited.append(source)
    start.append([source, count])
    if source not in graph:
        count += 1
        end.append([source, count])
        return None
    for node in graph[source]:
        if node not in visited:
            DFS(graph, node)
    count += 1
    end.append([source, count])


Graph = {}
visited = []
visited2 = []
end = []
start = []
visit = []
templist = []

# Inputting the graph edges.
numEdges = int(input().strip())
for i in range(numEdges):
    n1, n2 = list(map(int, input().strip().split()))
    Graph.setdefault(n1, []).append(n2)

# Completing DFS on graph.
so = int(input("Enter source: "))
DFS(Graph, so)
for node in Graph:
    if node not in visited:
        DFS(Graph, node)
print(start)
print(end)
print(visited)
visited2 = copy.deepcopy(visited)

#Sorting the ending times
end.sort(key= lambda row:row[1], reverse=True)

#Reversing the Graph's edge direction
Graph2 = {}
for key, values in Graph.items():
    for value in values:
        Graph2.setdefault(value, []).append(key)

#DFS again on the reversed components
visited[:] = []
cunt = 0
visit.append([])
for node, end_time in end:
    if node not in visited:
        DFS(Graph2, node)
        cunt += 1
        templist = copy.deepcopy(set(visited))
        for ab in range(0, cunt):
            templist -= set(visit[ab])
        visit.append(copy.deepcopy(templist))

print("Strongly Connected Components are:", visit[1:])