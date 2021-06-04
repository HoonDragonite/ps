from collections import deque

n, m, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for e in graph:
    e.sort()

# 그래프 출력
print("\n***** Graph *****")
print(graph)
print("***** Graph *****\n")

x = 1
q = deque([x])
visited = [False] * (n + 1)
visited[x] = True
print(q)


