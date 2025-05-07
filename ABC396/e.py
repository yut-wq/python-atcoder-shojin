from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    x = x - 1
    y = y - 1
    graph[x].append((y, z))
    graph[y].append((x, z))

visited = [False] * n
val = [-1] * n


def bfs(start):
    dq = deque([start])
    visited[start] = True
    comp = [start]
    while dq:
        now_point = dq.popleft()
        for next_point, label in graph[now_point]:
            if not visited[next_point]:
                visited[next_point] = True
                val[next_point] = val[now_point] ^ label
                comp.append(next_point)
                dq.append(next_point)
            else:
                if val[next_point] != val[now_point] ^ label:
                    print("-1")
                    exit()
    return comp


ans = [0] * n
for start in range(n):
    if visited[start]:
        continue
    val[start] = 0
    comp = bfs(start)
    for i in range(30):
        count = 0
        for j in comp:
            if val[j] & (1 << i):
                count += 1
        if count < len(comp) - count:
            for j in comp:
                if val[j] & (1 << i):
                    ans[j] = ans[j] | 1 << i
        else:
            for j in comp:
                if not (val[j] & (1 << i)):
                    ans[j] = ans[j] | 1 << i

# コメントアウトのコードでは[0, 1, 2]のように出力される
# print(ans)
# 下記のコードでは0 1 2のように出力される
print(*ans)
