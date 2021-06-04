from collections import deque

''' Depth First Search (DFS) '''
def dfs(x):
    print(x, end=' ')
    visited[x] = True
    for y in graph[x]: # x와 연결된 노드 중
        if not(visited[y]): # 방문안한 것이 있으면
            dfs(y)

''' Breadth First Search (BFS) '''
def bfs(x):
    q = deque([x])
    visited[x] = True
    while q:
        x = q.popleft()
        print(x, end=' ')
        for y in graph[x]: # x와 연결된 노드 중
            if not visited[y]: # 방문안한 것이 있으면
                q.append(y)
                visited[y] = True

# 자료입력
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
print("\n***** Graph *****")
print(graph)
print("***** Graph *****\n")

# DFS
visited = [False] * (n + 1) # 방문여부저장배열, 인덱스가 아닌 숫자 그대로 체크
dfs(start)

print()

# BFS
visited = [False] * (n + 1)
bfs(start)

'''
정리

BFS
 - 노드를 방문하면서 인접한 노드 중 방문하지 않았던 노드만 큐에 넣어 먼저 큐에 들어있던 노드부터 방문하면 되는 것
'''

'''
[최초 Graph의 형태, 노드배열이 연결된노드배열을 갖는 이차원배열]
graph[0] = []
graph[1] = [2, 3, 4]
graph[2] = [1, 4]
graph[3] = [1, 4]
graph[4] = [1, 2, 3]

[최초 visit의 형태]
visit = [False, False, False, False, False]

[q의 형태]
Root부터 시작해서 루트와 연결되어있는 노드를 큐에 넣음
for문 끝날때마다 다음 레벨

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