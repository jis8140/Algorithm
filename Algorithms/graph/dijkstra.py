from collections import defaultdict
import heapq


def dijkstra(adjacency_list: list, v: int):
    graph = defaultdict(list)

    for u, v, w in adjacency_list:
        graph[u].append((v, w))
        graph[v].append((u, w))

    queue = [(0, v)]
    weight = defaultdict(int)

    while queue:
        acc_w, node = heapq.heappop(queue)

        if node not in weight:
            weight[node] = acc_w
            for v, w in graph[node]:
                heapq.heappush(queue, (v, acc_w + w))

    if len(weight):
        return max(weight.values())

    return -1
