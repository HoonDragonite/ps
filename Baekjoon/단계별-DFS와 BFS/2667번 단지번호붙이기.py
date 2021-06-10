from collections import deque

def bfs_queue(n, k, visited=[]):
    q = deque([n])
    while q:
        n = q.popleft()
        print("n : " + str(n))
        if n not in visited:
            visited.append(n)
            if n-1 == k or n+1 == k or n*2 == k:
                return visited
            
            dis = [abs(k - (n+1)), abs(k - (n-1)), abs(k - n*2)]
            print(dis)
            pos = dis.index(min(dis))
            if pos == 0:
                q.append(n+1)
            elif pos == 1:
                q.append(n-1)
            elif pos == 2:
                q.append(n*2)
        if n == 999:
            return [2,2,2]
    return visited

n, k = map(int, input().split()) # 5 17 -> 4

print(len(bfs_queue(n, k)))