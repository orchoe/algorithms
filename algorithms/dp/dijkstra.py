import heapq
import math


def init_distance(graph, s):
    distance = {s: 0}
    for vertex in graph:
        if vertex != s:
            # 未知节点距离初始化为正无穷
            distance[vertex] = math.inf
    return distance


def dijkstra(graph, start):
    pri_queue = []
    # 使用一个优先队列，以保证距离最短的排列在第一位（第一个参数为距离，第二个为节点名称）
    heapq.heappush(pri_queue, (0, start))
    seen = set()
    parent = {start: None}
    distance = init_distance(graph, start)

    while len(pri_queue) > 0:
        pair = heapq.heappop(pri_queue)
        dist = pair[0]
        vertex = pair[1]
        # 将该节点标记为已查看
        seen.add(vertex)

        nodes = graph[vertex].keys()
        for node in nodes:
            if node not in seen:
                new_dist = dist + graph[vertex][node]
                if new_dist < distance[node]:
                    # 将该节点及与起始节点的距离推入优先队列
                    heapq.heappush(pri_queue, (new_dist, node))
                    parent[node] = vertex
                    distance[node] = new_dist

    return parent, distance


def test():
    graph = {
        'A': {'B': 5, 'C': 1},
        'B': {'A': 5, 'C': 2, 'D': 1},
        'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
        'D': {'B': 2, 'C': 4, 'E': 3, 'F': 6},
        'E': {'C': 8, 'D': 3},
        'F': {'D': 6}
    }

    parent, distance = dijkstra(graph, 'B')
    print(parent)
    print(distance)


test()
