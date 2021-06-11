from collections import deque

def bfs_queue(n, k, visited=[]):
    q = deque([n])
    while q:
        n = q.popleft()
        if n not in visited:
            visited.append(n) # 현재 n 
            print("n : " + str(n))
            for y in [n+1, n-1, n*2]:
                if k == y:
                    return visited
                else:
                    if y not in visited:
                        q.append(y)
    return visited

n, k = map(int, input().split()) # 5 17 -> 4

print(bfs_queue(n, k))
print(len(bfs_queue(n, k)))