def dfs_recursive(x, visited=[]):
    visited.append(x)
    for n in graph[x]:
        if n not in visited:
            dfs_recursive(n, visited)
    return visited

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
for e in graph:
    e.sort()

start = 1
print(len(dfs_recursive(start)) - 1)