from collections import deque

def dfs_recursive(x, visited=[]):
    visited.append(x)
    for n in graph[x]:
        if n not in visited:
            dfs_recursive(n, visited)
    return visited

def bfs_queue(x, visited=[]):
    q = deque([x])
    while q:
        n = q.popleft()
        if n not in visited:
            visited.append(n)
            for y in graph[n]:
                if y not in visited:
                    q.append(y)
    return visited

# 자료 입력
n, m, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 그래프 초기화 
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
for e in graph:
    e.sort()

# 그래프 출력
print(graph)

# 탐색 시작
print(dfs_recursive(start))
print(bfs_queue(start))

'''
[Input Example 1]
4 5 1
1 2
1 3
1 4
2 4
3 4
[Output Example 1]
1 2 4 3 
1 2 3 4
'''