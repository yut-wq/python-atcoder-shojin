point_count, side_count = map(int, input().split())

# 隣接頂点リスト．（頂点, 辺のラベル）をペアで持つ．
graph = [[] * point_count for i in range(point_count)]
for _ in range(side_count):
    point1, point2, label = map(int, input().split())
    point1 -= 1
    point2 -= 1
    graph[point1].append((point2, label))
    graph[point2].append((point1, label))

ans = 1 << 60
visited = [False] * point_count  # 訪問済みかどうかを持つリスト


def dfs(point, now_value):
    global ans
    visited[point] = True  # 頂点 v を訪問済みにする

    # もし今いる頂点が N - 1 なら答えを更新する
    if point == point_count - 1:
        ans = min(ans, now_value)

    for new_point, label in graph[point]:
        # もし頂点 u に訪れていないなら，頂点 u に進む
        if not visited[new_point]:
            dfs(new_point, now_value ^ label)
    visited[point] = False  # 訪問済みを解除する


dfs(0, 0)
print(ans)
